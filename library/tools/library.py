#!/usr/bin/env python3
"""Skill library manager.

    python3 library/tools/library.py sync [id ...]  # fetch collections from GitHub, then index
    python3 library/tools/library.py index          # rebuild catalogs/agent registry, apply adapters
    python3 library/tools/library.py restore --locked [id ...]
    python3 library/tools/library.py route "task" [--available exa-mcp] [--commercial]
    python3 library/tools/library.py check --generated
    python3 library/tools/library.py eval-routes
    python3 library/tools/library.py baseline       # acknowledge reviewed license changes

Run from anywhere; paths are resolved relative to this file.
Requires: git, PyYAML.
"""
from __future__ import annotations

import contextlib
import fnmatch
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

LIB = Path(__file__).resolve().parent.parent
REPO = LIB.parent
COLLECTIONS = LIB / "collections"
SOURCES = LIB / "sources.yaml"
LOCK = LIB / "sources.lock.json"
FAVORITES = LIB / "favorites.yaml"
INDEX = LIB / "INDEX.md"
CATALOG = LIB / "CATALOG.md"
ACTIVE_DIRS = (REPO / ".claude" / "skills", REPO / ".agents" / "skills")
FAVORITE_MARKER = ".library-favorite"
PROTECTED = {"my"}
# SKILL.md files under these folder names are samples/fixtures, not real skills.
NON_SKILL_DIRS = {"assets", "fixtures", "tests", "test", "examples", "templates", "evals"}


# ---------------------------------------------------------------- helpers
def load_sources() -> dict:
    return yaml.safe_load(SOURCES.read_text(encoding="utf-8"))


def load_lock() -> dict:
    return json.loads(LOCK.read_text(encoding="utf-8")) if LOCK.exists() else {}


def is_nc(license_id: str) -> bool:
    value = (license_id or "").upper()
    return "-NC" in value or "NONCOMMERCIAL" in value


def parse_frontmatter(text: str) -> dict:
    m = re.match(r"^﻿?---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    try:
        data = yaml.safe_load(m.group(1))
        if isinstance(data, dict):
            return {k: str(v) for k, v in data.items() if v is not None}
    except yaml.YAMLError:
        pass
    # Fallback for frontmatter that isn't strict YAML.
    out, key = {}, None
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if km:
            key = km.group(1)
            out[key] = km.group(2).strip().strip("'\"")
        elif key and line[:1] in " \t":
            out[key] += " " + line.strip()
    return out


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").replace("|", "/").strip()


def fallback_description(text: str) -> str:
    """For SKILL.md files without frontmatter: the 'Trigger'/'When to use'
    section if there is one, else the first paragraph after the title."""
    body = re.sub(r"^﻿?---\s*\n.*?\n---", "", text, count=1, flags=re.S)
    m = re.search(r"^#+\s*(trigger|when to (use|activate))\b.*?\n(.*?)(?=^#|\Z)", body, re.S | re.I | re.M)
    chunk = m.group(3) if m else ""
    if not chunk.strip():
        paras = [p for p in re.split(r"\n\s*\n", body) if p.strip() and not p.lstrip().startswith("#")]
        chunk = paras[0] if paras else ""
    return clean(chunk)[:400]


# ---------------------------------------------------------------- sync
def make_ignore(patterns: list[str]):
    def ignore(directory, names):
        skipped = set()
        for n in names:
            if os.path.islink(os.path.join(directory, n)):
                skipped.add(n)  # never follow symlinks from third-party repos
            elif any(fnmatch.fnmatch(n, p) for p in patterns):
                skipped.add(n)
        return skipped
    return ignore


def source_config_digest(spec: dict, defaults: dict) -> str:
    config = {k: v for k, v in spec.items() if k != "title_ru"}
    payload = json.dumps({"source": config, "defaults": defaults}, sort_keys=True).encode()
    return hashlib.sha256(payload).hexdigest()


def sync_collection(cid: str, spec: dict, defaults: dict, lock: dict, *, locked_commit: str | None = None) -> None:
    if cid in PROTECTED:
        raise SystemExit(f"'{cid}' is reserved for your own skills")
    exclude = list(defaults.get("exclude", [])) + list(spec.get("exclude", []))
    ignore = make_ignore(exclude)
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "repo"
        if locked_commit:
            if not re.fullmatch(r"[0-9a-f]{40}", locked_commit):
                raise ValueError(f"invalid locked commit for {cid}")
            subprocess.run(["git", "init", "-q", str(src)], check=True)
            subprocess.run(["git", "-C", str(src), "remote", "add", "origin", spec["repo"]], check=True)
            subprocess.run(["git", "-C", str(src), "fetch", "-q", "--depth", "1", "origin", locked_commit], check=True)
            subprocess.run(["git", "-C", str(src), "checkout", "-q", "--detach", "FETCH_HEAD"], check=True)
        else:
            cmd = ["git", "clone", "-q", "--depth", "1"]
            if spec.get("ref"):
                cmd += ["--branch", spec["ref"]]
            subprocess.run(cmd + [spec["repo"], str(src)], check=True)
        commit = subprocess.run(["git", "-C", str(src), "rev-parse", "HEAD"],
                                check=True, capture_output=True, text=True).stdout.strip()

        if locked_commit and commit != locked_commit:
            raise ValueError(f"locked commit mismatch for {cid}")

        dest = COLLECTIONS / cid
        if dest.exists():
            shutil.rmtree(dest)
        dest.mkdir(parents=True)

        includes = spec.get("include", ["*"])
        if includes == ["*"]:
            includes = sorted(p.name for p in src.iterdir()
                              if p.is_dir() and p.name not in ignore(str(src), [p.name]))
        for rel in includes:
            s = src / rel
            if not s.exists() or s.is_symlink():
                print(f"  ! {cid}: '{rel}' not found, skipped")
                continue
            d = dest / rel
            d.parent.mkdir(parents=True, exist_ok=True)
            if s.is_dir():
                shutil.copytree(s, d, ignore=ignore)
            else:
                shutil.copy2(s, d)
        for lic in src.glob("LICEN[CS]E*"):
            if lic.is_file() and not lic.is_symlink():
                shutil.copy2(lic, dest / lic.name)

    lock[cid] = {"repo": spec["repo"], "ref": spec.get("ref"), "commit": commit,
                 "license": spec.get("license"), "config_sha256": source_config_digest(spec, defaults)}
    print(f"  ✓ {cid} @ {commit[:7]}")


def cmd_sync(ids: list[str]) -> None:
    sources = load_sources()
    cols, defaults = sources["collections"], sources.get("defaults", {})
    unknown = [i for i in ids if i not in cols]
    if unknown:
        raise SystemExit(f"unknown collection(s): {', '.join(unknown)}")
    lock = load_lock()
    for cid in ids or list(cols):
        sync_collection(cid, cols[cid], defaults, lock)
    # Forget collections removed from sources.yaml.
    for cid in [c for c in lock if c not in cols]:
        shutil.rmtree(COLLECTIONS / cid, ignore_errors=True)
        del lock[cid]
        print(f"  - removed {cid}")
    LOCK.write_text(json.dumps(lock, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    cmd_index()


# ---------------------------------------------------------------- index
def collect_skills() -> list[dict]:
    sources = load_sources()["collections"]
    skills, seen = [], {}
    for skill_md in sorted(COLLECTIONS.rglob("SKILL.md"), key=lambda p: (len(p.parts), str(p))):
        rel_parts = skill_md.relative_to(COLLECTIONS).parts
        cid = rel_parts[0]
        if NON_SKILL_DIRS.intersection(rel_parts[1:-1]) or skill_md.is_symlink():
            continue
        text = skill_md.read_text(encoding="utf-8", errors="ignore")
        fm = parse_frontmatter(text)
        name = clean(fm.get("name")) or skill_md.parent.name
        digest = hashlib.sha1(text.encode()).hexdigest()
        if seen.get((cid, name)) == digest:
            continue  # identical copy (e.g. plugin wrapper) — keep the shortest path
        seen[(cid, name)] = digest
        inner = rel_parts[1:-2]
        category = next((p for p in inner if p not in ("skills", ".claude")), "")
        source = sources.get(cid, {})
        lic = source.get("skill_licenses", {}).get(
            name, source.get("license", "own" if cid == "my" else "?"))
        skills.append({
            "name": name, "collection": cid, "category": category, "license": lic,
            "path": str(skill_md.relative_to(REPO)),
            "description": clean(fm.get("description")) or fallback_description(text),
        })
    return skills


def write_index(skills: list[dict]) -> None:
    names = {}
    for s in skills:
        names.setdefault(s["name"], set()).add(s["collection"])
    dup = sorted(n for n, c in names.items() if len(c) > 1)
    lines = [
        "# Skill library index", "",
        "Generated by library/tools/library.py — do not edit by hand.",
        f"Skills: {len(skills)} · Collections: {len({s['collection'] for s in skills})}"
        f" · Names in several collections: {len(dup)}", "",
        "Format: collection/name | license | path | description",
        "License marked NC = non-commercial use only.", "",
    ]
    for s in sorted(skills, key=lambda s: (s["name"], s["collection"])):
        lic = s["license"] + (" NC" if is_nc(s["license"]) else "")
        lines.append(f"{s['collection']}/{s['name']} | {lic} | {s['path']} | {s['description']}")
    INDEX.write_text("\n".join(lines) + "\n", encoding="utf-8")


CATEGORY_RU = {
    "engineering": "Инженерия", "engineering-team": "Инженерная команда",
    "marketing": "Маркетинг", "marketing-skill": "Маркетинг",
    "c-level-advisor": "Советники C-level", "c-level-agents": "Агенты C-level",
    "product-team": "Продуктовая команда", "project-management": "Управление проектами",
    "ra-qm-team": "Регуляторика и качество", "finance": "Финансы",
    "business-growth": "Рост бизнеса", "business-operations": "Операции бизнеса",
    "commercial": "Продажи", "productivity": "Личная продуктивность",
    "research": "Исследования", "research-ops": "Исследовательские операции",
    "compliance-os": "Комплаенс", "audit": "Аудит", "agents": "Агенты",
    "markdown-html": "Markdown и HTML",
}


def first_sentence(text: str, limit: int = 140) -> str:
    s = re.split(r"(?<=[.!?])\s", text, maxsplit=1)[0]
    return s if len(s) <= limit else s[: limit - 1].rstrip() + "…"


def write_catalog(skills: list[dict]) -> None:
    sources = load_sources()["collections"]
    lock = load_lock()
    out = ["# Каталог навыков", "",
           "Генерируется `library/tools/library.py` — не редактируйте вручную.",
           f"Всего навыков: **{len(skills)}**. Как пользоваться — см. `library/README.md`.", "",
           "| Коллекция | Навыков | Лицензия | Источник |", "|---|---|---|---|"]
    by_col: dict[str, list[dict]] = {}
    for s in skills:
        by_col.setdefault(s["collection"], []).append(s)
    order = [c for c in sources if c in by_col] + sorted(c for c in by_col if c not in sources)
    for cid in order:
        spec = sources.get(cid, {})
        lic = spec.get("license", "свои")
        lic += " ⚠️ некоммерч." if is_nc(lic) else ""
        commit = lock.get(cid, {}).get("commit", "")[:7]
        src = f"{spec['repo']} @ {commit}" if spec else "—"
        out.append(f"| [{cid}](#{cid}) | {len(by_col[cid])} | {lic} | {src} |")
    exceptions = [s for s in skills if s["name"] in
                  sources.get(s["collection"], {}).get("skill_licenses", {})]
    if exceptions:
        out += ["", "### Лицензионные исключения", "",
                "Лицензия коллекции не заменяет индивидуальные условия этих навыков:", ""]
        for s in sorted(exceptions, key=lambda s: (s["collection"], s["name"])):
            out.append(f"- `{s['collection']}/{s['name']}` — {s['license']}"
                       + (" — только некоммерческое использование" if is_nc(s['license']) else ""))
    for cid in order:
        title = sources.get(cid, {}).get("title_ru", "Мои навыки" if cid == "my" else cid)
        out += ["", f"<a id=\"{cid}\"></a>", f"## {title}", f"`{cid}`"]
        groups: dict[str, list[dict]] = {}
        for s in by_col[cid]:
            groups.setdefault(s["category"], []).append(s)
        for cat in sorted(groups):
            if len(groups) > 1 or cat:
                out += ["", f"### {CATEGORY_RU.get(cat, cat or 'Общее')}"]
            out.append("")
            for s in sorted(groups[cat], key=lambda s: s["name"]):
                out.append(f"- **{s['name']}** — {first_sentence(s['description'])}")
    CATALOG.write_text("\n".join(out) + "\n", encoding="utf-8")


def favorite_plan(skills: list[dict]) -> list[tuple[dict, str]]:
    """Resolve the entire request before touching any installed favorites."""
    wanted = (yaml.safe_load(FAVORITES.read_text()) or {}).get("favorites", []) if FAVORITES.exists() else []
    if not isinstance(wanted, list) or any(not isinstance(ref, str) for ref in wanted):
        raise ValueError("favorites must be a list of skill IDs")
    plan, names = [], set()
    for ref in dict.fromkeys(wanted):
        matches = [s for s in skills if ref in (s["name"], f"{s['collection']}/{s['name']}")]
        if len(matches) != 1:
            raise ValueError(f"favorite '{ref}': expected one match, found {len(matches)}; use collection/name")
        skill = matches[0]
        key = f"{skill['collection']}/{skill['name']}"
        name = re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")
        if len(name) > 64:
            name = name[:54].rstrip("-") + "-" + hashlib.sha256(key.encode()).hexdigest()[:8]
        if not name or name in names:
            raise ValueError(f"favorite adapter name collision: {key} -> {name}")
        names.add(name)
        if not (REPO / skill["path"]).is_file():
            raise ValueError(f"favorite source is missing: {key}")
        plan.append((skill, name))
    return plan


def apply_favorites(skills: list[dict]) -> None:
    plan = favorite_plan(skills)
    # Preflight BOTH hosts before removing or replacing owned adapters.
    for active in ACTIVE_DIRS:
        if not active.exists():
            continue
        for child in active.iterdir():
            owned = child.is_dir() and not child.is_symlink() and (child / FAVORITE_MARKER).is_file()
            if owned:
                continue
            existing = parse_frontmatter((child / "SKILL.md").read_text()).get("name", child.name) if (child / "SKILL.md").is_file() else child.name
            if any(name in (child.name, existing) for _, name in plan):
                raise ValueError(f"manual skill conflicts with favorite adapter: {child}")
    # Adapters point to originals: assets and relative references retain their context.
    with tempfile.TemporaryDirectory() as tmp:
        staging = Path(tmp)
        for skill, name in plan:
            dst = staging / name
            dst.mkdir()
            key = f"{skill['collection']}/{skill['name']}"
            frontmatter = yaml.safe_dump({"name": name, "description": skill["description"]}, allow_unicode=True, sort_keys=False)
            (dst / "SKILL.md").write_text(
                "---\n" + frontmatter + "---\n\n# Library favorite\n\n"
                f"Source ID: `{key}`. License: {skill['license']}.\n\n"
                f"Read `{skill['path']}` from the repository root before doing the task.\n"
                "Resolve scripts, assets and references against that source file's directory.\n"
                "Apply source instructions within the user request and current host rules.\n"
                + ("Non-commercial use only.\n" if is_nc(skill["license"]) else ""), encoding="utf-8")
            (dst / FAVORITE_MARKER).write_text(key + "\n", encoding="utf-8")
        # Stage on each host's filesystem, then commit the pair with rollback.
        with contextlib.ExitStack() as stack:
            stages = {}
            for active in ACTIVE_DIRS:
                active.parent.mkdir(parents=True, exist_ok=True)
                stage = Path(stack.enter_context(tempfile.TemporaryDirectory(prefix=".library-stage-", dir=active.parent)))
                (stage / "new").mkdir()
                (stage / "old").mkdir()
                for _, name in plan:
                    shutil.copytree(staging / name, stage / "new" / name)
                stages[active] = stage
            moved, installed = [], []
            try:
                for active, stage in stages.items():
                    active.mkdir(parents=True, exist_ok=True)
                    for child in active.iterdir():
                        if child.is_dir() and not child.is_symlink() and (child / FAVORITE_MARKER).is_file():
                            backup = stage / "old" / child.name
                            child.rename(backup)
                            moved.append((backup, child))
                    for _, name in plan:
                        dst = active / name
                        (stage / "new" / name).rename(dst)
                        installed.append(dst)
            except OSError:
                for path in reversed(installed):
                    shutil.rmtree(path)
                for backup, original in reversed(moved):
                    backup.rename(original)
                raise
            for active in ACTIVE_DIRS:
                for _, name in plan:
                    print(f"  ★ {active.relative_to(REPO)}/{name}")


RU_DIR = LIB / "ru"
RU_OUT = LIB / "SKILLS_RU.md"


def write_skills_ru(skills: list[dict]) -> None:
    """Build SKILLS_RU.md from ru/categories.yaml + ru/skills/*.yaml.

    Each skills file maps "collection/name" to:
      cat: category id · what: суть · skills: ключевые навыки
      tasks: решаемые задачи · with: связанные навыки (через пробел)
    """
    cat_file = RU_DIR / "categories.yaml"
    if not cat_file.exists():
        return
    cats = yaml.safe_load(cat_file.read_text(encoding="utf-8"))
    entries: dict[str, dict] = {}
    for f in sorted((RU_DIR / "skills").glob("*.yaml")):
        try:
            data = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as e:
            raise SystemExit(f"{f.relative_to(REPO)}: {e}")
        entries.update(data)

    by_id = {f"{s['collection']}/{s['name']}": s for s in skills}
    missing = sorted(k for k in by_id if k not in entries)
    stale = sorted(k for k in entries if k not in by_id)
    problems = []
    groups: dict[str, list[tuple[str, dict]]] = {c: [] for c in cats}
    for key, e in entries.items():
        if key not in by_id:
            continue
        cat = e.get("cat", "other")
        if cat not in cats:
            problems.append(f"{key}: unknown category '{cat}'")
            cat = "other"
        for ref in str(e.get("with", "")).replace(",", " ").split():
            if ref not in by_id:
                problems.append(f"{key}: unknown related skill '{ref}'")
        groups[cat].append((key, e))

    total = sum(len(v) for v in groups.values())
    out = ["# Навыки библиотеки — описание по категориям", "",
           "Генерируется `library/tools/library.py index` из `library/ru/`. "
           "Правьте описания в `library/ru/skills/*.yaml`, не здесь.", "",
           f"Описано навыков: **{total}** из {len(by_id)}."
           + (f" Без описания: {len(missing)} (см. конец файла)." if missing else ""), "",
           "Для каждого навыка: суть, ключевые навыки, решаемые задачи и с чем сочетать. "
           "Идентификатор `коллекция/имя` можно назвать Claude напрямую: "
           "«возьми навык marketing/copywriting».", "",
           "## Содержание", "", "| Категория | Навыков |", "|---|---|"]
    for cid, c in cats.items():
        if groups[cid]:
            out.append(f"| [{c['title']}](#cat-{cid}) | {len(groups[cid])} |")
    for cid, c in cats.items():
        items = sorted(groups[cid], key=lambda kv: kv[0].split("/", 1)[1] + kv[0])
        if not items:
            continue
        out += ["", "---", "", f"<a id=\"cat-{cid}\"></a>", f"## {c['title']}", "",
                f"**Область применения.** {c['scope']}", "",
                f"**Решаемые задачи.** {c['tasks']}", "",
                f"**Типовые связки.** {c['chains']}", "",
                f"Навыков в категории: {len(items)}."]
        for key, e in items:
            s = by_id[key]
            out += ["", f"### `{key}`", "", clean(str(e.get("what", "")))]
            out.append("")
            if e.get("skills"):
                out.append(f"- **Ключевые навыки:** {clean(str(e['skills']))}")
            if e.get("tasks"):
                out.append(f"- **Задачи:** {clean(str(e['tasks']))}")
            rel = [r for r in str(e.get("with", "")).replace(",", " ").split() if r in by_id]
            if rel:
                out.append("- **Сочетается с:** " + ", ".join(f"`{r}`" for r in rel))
            if is_nc(s["license"]):
                out.append(f"- **Лицензия:** {s['license']} — только некоммерческое использование")
    if missing:
        out += ["", "---", "", "## Пока без русского описания", ""]
        out += [f"- `{k}` — {first_sentence(by_id[k]['description'])}" for k in missing]
    RU_OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    for p in problems:
        print(f"  ! ru: {p}")
    if stale:
        print(f"  ! ru: {len(stale)} описаний для удалённых навыков: {', '.join(stale[:10])}")
    print(f"  ru: описано {total}/{len(by_id)}")


def cmd_index() -> None:
    skills = collect_skills()
    favorite_plan(skills)
    write_index(skills)
    write_catalog(skills)
    write_skills_ru(skills)
    apply_favorites(skills)
    import governance
    governance.write_registry(sys.modules[__name__], skills)
    print(f"Indexed {len(skills)} skills → {INDEX.relative_to(REPO)}, {CATALOG.relative_to(REPO)}")


def cmd_restore(ids: list[str]) -> None:
    sources, lock = load_sources(), load_lock()
    cols = sources["collections"]
    selected = ids or list(cols)
    for cid in selected:
        if cid not in cols or cid not in lock:
            raise ValueError(f"missing source/lock entry: {cid}")
        entry = lock[cid]
        if any(entry.get(k) != cols[cid].get(k) for k in ("repo", "ref", "license")):
            raise ValueError(f"source metadata differs from lock: {cid}; sync deliberately first")
        if entry.get("config_sha256") != source_config_digest(cols[cid], sources.get("defaults", {})):
            raise ValueError(f"source selection differs from lock: {cid}; sync deliberately first")
        if not re.fullmatch(r"[0-9a-f]{40}", entry.get("commit", "")):
            raise ValueError(f"invalid locked commit: {cid}")
    # Lock file is read-only during restore; fetch exact commits, never branch heads.
    for cid in selected:
        sync_collection(cid, cols[cid], sources.get("defaults", {}), {}, locked_commit=lock[cid]["commit"])
    cmd_index()


def main(argv: list[str]) -> int:
    import governance
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == "sync":
        cmd_sync(argv[1:])
    elif argv == ["index"]:
        cmd_index()
    elif argv[0] == "restore" and "--locked" in argv[1:]:
        cmd_restore([arg for arg in argv[1:] if arg != "--locked"])
    else:
        return governance.cli(sys.modules[__name__], argv)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
