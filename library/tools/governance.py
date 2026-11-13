"""Routing, agent inventory and offline library checks. Does not execute source skills."""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import contextlib
import hashlib
import io
import json
from pathlib import Path
import re
import tempfile
import yaml


def skill_id(skill):
    return f"{skill['collection']}/{skill['name']}"


def load_routes(lib):
    path = lib.LIB / 'routing.yaml'
    return (yaml.safe_load(path.read_text()) or {}).get('routes', []) if path.exists() else []


def resolve(lib, query, *, available=None, commercial=False, intent=None, skills=None):
    skills = skills if skills is not None else lib.collect_skills()
    by_id = {skill_id(s): s for s in skills}
    # Explicit qualified IDs override automatic ranking. Never substitute a different skill.
    explicit = list(dict.fromkeys(re.findall(r'(?<![\w/-])([a-z0-9][a-z0-9-]*/[a-z0-9][a-z0-9-]*)(?![\w/-])', query)))
    if explicit:
        candidates = [{'skill': sid, 'requires': []} for sid in explicit]
        route = None
        # Capability declarations apply even for an explicitly selected skill.
        known = defaultdict(list)
        for r in load_routes(lib):
            known[r['primary']].append(r.get('requires', []))
            for a in r.get('alternatives', []):
                known[a['skill']].append(a.get('requires', []))
        for c in candidates:
            choices = known.get(c['skill'], [[]])
            c['requires'] = min(choices, key=lambda req: (len(set(req) - set(available or [])), len(req)))
        requested = explicit
    else:
        hits = []
        for r in load_routes(lib):
            matches = [m for pattern in r.get('match', []) if (m := re.search(pattern, query, re.I))]
            if (intent and r['id'] == intent) or (not intent and matches):
                if not intent and any(re.search(p, query, re.I) for p in r.get('exclude', [])):
                    continue
                hits.append((r.get('priority', 0), sum(len(m.group()) for m in matches), r))
        if not hits:
            return {'status': 'no_route', 'primary': None, 'reason': 'Search INDEX.md; do not invent a route.'}
        hits.sort(key=lambda h: (-h[0], -h[1], h[2]['id']))
        best = hits[0]
        if len(hits) > 1 and best[:2] == hits[1][:2] and best[2]['primary'] != hits[1][2]['primary']:
            return {'status': 'ambiguous', 'primary': None, 'routes': [h[2]['id'] for h in hits if h[:2] == best[:2]]}
        route = best[2]
        preferred, fallback = [], []
        for alt in route.get('alternatives', []):
            if alt.get('when'):
                if any(re.search(p, query, re.I) for p in alt['when']):
                    preferred.append(alt)
            else:
                fallback.append(alt)
        candidates = preferred + [{'skill': route['primary'], 'requires': route.get('requires', [])}] + fallback
        requested = None
    rejected = []
    selected = []
    for c in candidates:
        sid = c['skill']
        if sid not in by_id:
            rejected.append({'skill': sid, 'reason': 'unknown_skill'})
        elif commercial and lib.is_nc(by_id[sid]['license']):
            rejected.append({'skill': sid, 'reason': 'noncommercial'})
        elif c.get('requires') and available is None:
            rejected.append({'skill': sid, 'reason': 'capabilities_not_declared', 'requires': c['requires']})
        elif set(c.get('requires', [])) - set(available or []):
            rejected.append({'skill': sid, 'reason': 'missing_capabilities', 'requires': sorted(set(c['requires']) - set(available or []))})
        else:
            selected.append(sid)
            if not explicit:
                break
    if explicit and len(selected) != len(requested):
        return {'status': 'blocked', 'primary': None, 'requested': requested, 'rejected': rejected}
    if not selected:
        return {'status': 'blocked', 'primary': None, 'route': route['id'] if route else None, 'rejected': rejected}
    first = by_id[selected[0]]
    return {'status': 'selected', 'route': route['id'] if route else None, 'explicit': bool(explicit),
            'primary': selected[0], 'additional': selected[1:], 'path': first['path'],
            'license': first['license'], 'noncommercial': lib.is_nc(first['license']), 'rejected': rejected}


def agent_inventory(lib, skills):
    groups = defaultdict(list)
    for p in sorted(lib.COLLECTIONS.rglob('*.md')):
        relative = p.relative_to(lib.COLLECTIONS)
        if 'agents' not in relative.parts[:-1] or p.is_symlink():
            continue
        groups[hashlib.sha256(p.read_bytes()).hexdigest()].append(p)
    sources = [(s, (lib.REPO / s['path']).parent, (lib.REPO / s['path']).read_text(errors='replace')) for s in skills]
    source_refs = defaultdict(set)
    for s, parent, source in sources:
        for match in re.findall(r'agents/[A-Za-z0-9_./-]+\.md', source):
            source_refs[(parent / match).resolve()].add(skill_id(s))
    result = []
    for digest, paths in sorted(groups.items()):
        canonical = min(paths, key=lambda p: (len(p.parts), str(p)))
        text = canonical.read_text(errors='replace')
        fm = lib.parse_frontmatter(text)
        owners, references = set(), set()
        for s, parent, source in sources:
            if any(parent in p.parents for p in paths):
                owners.add(skill_id(s))
        for path in paths:
            references.update(source_refs.get(path, set()))
        kind = 'template' if 'TEMPLATE' in canonical.stem.upper() else ('documentation' if canonical.stem.upper() in {'README', 'CLAUDE', 'AGENTS'} else 'agent_instructions')
        result.append({'id': 'agent-' + digest[:16], 'sha256': digest, 'kind': kind,
                       'name': fm.get('name', canonical.stem),
                       'description': fm.get('description') or lib.fallback_description(text), 'tools': fm.get('tools', ''),
                       'source_licenses': {p.relative_to(lib.COLLECTIONS).parts[0]: lib.load_sources()['collections'].get(p.relative_to(lib.COLLECTIONS).parts[0], {}).get('license', 'own') for p in paths},
                       'paths': [str(p.relative_to(lib.REPO)) for p in paths],
                       'owner_skills': sorted(owners), 'referenced_by': sorted(references),
                       'host_registration': 'source-only; not auto-installed'})
    return sorted(result, key=lambda a: (a['name'], a['id']))


def write_registry(lib, skills, output_dir=None):
    agents = agent_inventory(lib, skills)
    dest = output_dir or lib.LIB
    dest.mkdir(parents=True, exist_ok=True)
    data = {'schema_version': 1, 'physical_files': sum(len(a['paths']) for a in agents), 'agents': agents}
    (dest / 'agents.index.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    lines = ['# Реестр агентных инструкций', '',
             'Генерируется `library/tools/library.py index`; не редактируйте вручную.', '',
             f"Файлов: {data['physical_files']}. Уникальных инструкций по SHA-256: {len(agents)}.", '',
             'Одинаковое содержимое объединено логически; исходные пути сохранены. Это реестр файлов, а не список запущенных или установленных агентов.', '',
             'Инструменты, потребляющие навыки и полные хеши: `agents.index.json`.', '',
             '| Инструкция / ID | Тип | Пути | Навыки-владельцы и прямые ссылки |', '|---|---|---|---|']
    for a in agents:
        paths = '<br>'.join(f"[{p}](../{p})" for p in a['paths'])
        refs = ', '.join(f'`{sid}`' for sid in sorted(set(a['owner_skills'] + a['referenced_by']))) or 'общие инструкции'
        lines.append(f"| {lib.clean(a['name'])}<br>`{a['id']}` | {a['kind']} | {paths} | {refs} |")
    (dest / 'AGENTS_INDEX.md').write_text('\n'.join(lines) + '\n')
    return data


def license_snapshot(lib, skills):
    return {skill_id(s): {'effective': s['license'],
                          'declared': lib.parse_frontmatter((lib.REPO / s['path']).read_text()).get('license', '')}
            for s in sorted(skills, key=skill_id)}


def audit(lib, *, generated=False):
    skills = lib.collect_skills()
    errors, warnings = [], []
    by_id, by_name, hashes = defaultdict(list), defaultdict(list), defaultdict(list)
    for s in skills:
        by_id[skill_id(s)].append(s)
        by_name[s['name']].append(s)
        hashes[hashlib.sha256((lib.REPO / s['path']).read_bytes()).hexdigest()].append(skill_id(s))
    for sid, group in by_id.items():
        if len(group) > 1:
            errors.append(f'duplicate skill ID: {sid}')
    routes = load_routes(lib)
    route_ids, covered = set(), set()
    for r in routes:
        if r['id'] in route_ids:
            errors.append(f"duplicate route ID: {r['id']}")
        route_ids.add(r['id'])
        candidates = [{'skill': r['primary']}] + r.get('alternatives', [])
        for c in candidates:
            covered.add(c['skill'])
            if c['skill'] not in by_id:
                errors.append(f"route {r['id']}: unknown skill {c['skill']}")
        for pattern in r.get('match', []) + r.get('exclude', []) + [p for a in r.get('alternatives', []) for p in a.get('when', [])]:
            try:
                re.compile(pattern)
            except re.error as exc:
                errors.append(f"route {r['id']}: {exc}")
    collisions = {name: [skill_id(s) for s in group] for name, group in by_name.items() if len(group) > 1}
    for name, ids in collisions.items():
        if set(ids) - covered:
            errors.append(f'unrouted name collision: {name}: {ids}')
    for group in hashes.values():
        if len(group) > 1:
            warnings.append('identical skill files: ' + ', '.join(group))
    try:
        lib.favorite_plan(skills)
    except ValueError as exc:
        errors.append(str(exc))
    entries, categories = {}, yaml.safe_load((lib.RU_DIR / 'categories.yaml').read_text())
    for path in sorted((lib.RU_DIR / 'skills').glob('*.yaml')):
        values = yaml.safe_load(path.read_text()) or {}
        for sid in values:
            if sid in entries:
                errors.append(f'duplicate Russian description: {sid}')
        entries.update(values)
    for sid, entry in entries.items():
        if sid not in by_id:
            errors.append(f'Russian description points to unknown skill: {sid}')
        if entry.get('cat') not in categories:
            errors.append(f'unknown category: {sid}: {entry.get("cat")}')
        for ref in str(entry.get('with', '')).replace(',', ' ').split():
            if ref not in by_id:
                errors.append(f'broken related skill: {sid} -> {ref}')
    for sid in sorted(set(by_id) - set(entries)):
        warnings.append(f'missing Russian description: {sid}')
    baseline_path = lib.LIB / 'audit-baseline.json'
    current = license_snapshot(lib, skills)
    baseline = json.loads(baseline_path.read_text()) if baseline_path.exists() else {}
    if not baseline:
        errors.append('missing audit-baseline.json; run baseline after reviewing licenses')
    for sid, previous in baseline.get('licenses', {}).items():
        if sid in current and current[sid] != previous:
            errors.append(f'license changed: {sid}; review and run baseline explicitly')
    for sid in sorted(set(current) - set(baseline.get('licenses', {}))):
        warnings.append(f'new skill requires license review: {sid}')
    # Short explicit NC declarations must not be hidden under a collection MIT license.
    for sid, item in current.items():
        declared = item['declared']
        if len(declared) < 80 and lib.is_nc(declared) and not lib.is_nc(item['effective']):
            errors.append(f'noncommercial declaration not reflected in index: {sid}')
    source = lib.load_sources()['collections']
    lock = lib.load_lock()
    for cid, spec in source.items():
        entry = lock.get(cid, {})
        if not re.fullmatch('[0-9a-f]{40}', entry.get('commit', '')):
            errors.append(f'missing/invalid locked commit: {cid}')
        if entry.get('config_sha256') != lib.source_config_digest(spec, lib.load_sources().get('defaults', {})):
            errors.append(f'source selection differs from lock: {cid}')
        if any(entry.get(k) != spec.get(k) for k in ('repo', 'ref', 'license')):
            errors.append(f'source and lock metadata differ: {cid}')
    if generated:
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            saved = {k: getattr(lib, k) for k in ('INDEX', 'CATALOG', 'RU_OUT')}
            try:
                lib.INDEX, lib.CATALOG, lib.RU_OUT = [dest / p.name for p in saved.values()]
                with contextlib.redirect_stdout(io.StringIO()):
                    lib.write_index(skills);lib.write_catalog(skills);lib.write_skills_ru(skills)
                write_registry(lib, skills, dest)
                for name in ['INDEX.md', 'CATALOG.md', 'SKILLS_RU.md', 'AGENTS_INDEX.md', 'agents.index.json']:
                    actual = lib.LIB / name
                    if not actual.exists() or actual.read_bytes() != (dest / name).read_bytes():
                        errors.append(f'generated artifact differs: {name}; run index')
            finally:
                for key, value in saved.items():
                    setattr(lib, key, value)
    agents = agent_inventory(lib, skills)
    return {'skills': len(skills), 'name_collisions': collisions,
            'agents': {'physical_files': sum(len(a['paths']) for a in agents), 'unique_records': len(agents),
                       'shared_instructions': [{'id': a['id'], 'paths': a['paths']} for a in agents if len(a['paths']) > 1]},
            'errors': errors, 'warnings': warnings}


def eval_routes(lib, cases_path=None):
    cases = yaml.safe_load((cases_path or lib.LIB / 'evals/routing.yaml').read_text())['cases']
    skills = lib.collect_skills()
    failures = []
    for case in cases:
        answers = [resolve(lib, case['query'], available=case.get('available'),
                           commercial=case.get('commercial', False), skills=skills) for _ in range(3)]
        expected = case.get('expected')
        if any(a != answers[0] for a in answers):
            failures.append({'case': case['id'], 'reason': 'unstable route'})
        if answers[0].get('primary') != expected or answers[0]['status'] != case.get('status', 'selected'):
            failures.append({'case': case['id'], 'expected': expected, 'actual': answers[0]})
    return {'kind': 'deterministic-router; not model evaluation', 'cases': len(cases),
            'repeats': 3, 'failures': failures}


def cli(lib, argv):
    parser = argparse.ArgumentParser(description='Library governance')
    commands = parser.add_subparsers(dest='command', required=True)
    route = commands.add_parser('route')
    route.add_argument('query');route.add_argument('--intent');route.add_argument('--available', default=None)
    route.add_argument('--commercial', action='store_true')
    check = commands.add_parser('check');check.add_argument('--generated', action='store_true')
    commands.add_parser('baseline');commands.add_parser('eval-routes')
    args = parser.parse_args(argv)
    if args.command == 'route':
        available = None if args.available is None else set(filter(None, args.available.split(',')))
        result = resolve(lib, args.query, available=available, commercial=args.commercial, intent=args.intent)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result['status'] == 'selected' else 1
    if args.command == 'baseline':
        (lib.LIB / 'audit-baseline.json').write_text(json.dumps({'schema_version': 1, 'licenses': license_snapshot(lib, lib.collect_skills())}, ensure_ascii=False, indent=2) + '\n')
        print('License baseline updated; review this change before committing.')
        return 0
    result = audit(lib, generated=args.generated) if args.command == 'check' else eval_routes(lib)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result.get('errors') or result.get('failures') else 0
