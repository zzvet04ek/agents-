#!/usr/bin/env python3
"""Skill library manager.

    python3 library/tools/library.py sync [id ...]  # fetch collections from GitHub, then index
    python3 library/tools/library.py index          # rebuild INDEX.md / CATALOG.md, apply favorites

Run from anywhere; paths are resolved relative to this file.
Requires: git, PyYAML.
"""
from __future__ import annotations

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
ACTIVE = REPO / ".claude" / "skills"
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
    return "-NC" in (license_id or "").upper()


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


def sync_collection(cid: str, spec: dict, defaults: dict, lock: dict) -> None:
    if cid in PROTECTED:
        raise SystemExit(f"'{cid}' is reserved for your own skills")
    exclude = list(defaults.get("exclude", [])) + list(spec.get("exclude", []))
    ignore = make_ignore(exclude)
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "repo"
        cmd = ["git", "clone", "-q", "--depth", "1"]
        if spec.get("ref"):
            cmd += ["--branch", spec["ref"]]
        subprocess.run(cmd + [spec["repo"], str(src)], check=True)
        commit = subprocess.run(["git", "-C", str(src), "rev-parse", "HEAD"],
                                check=True, capture_output=True, text=True).stdout.strip()

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
                 "license": spec.get("license")}
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
        lic = sources.get(cid, {}).get("license", "own" if cid == "my" else "?")
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


def apply_favorites(skills: list[dict]) -> None:
    wanted = []
    if FAVORITES.exists():
        wanted = (yaml.safe_load(FAVORITES.read_text(encoding="utf-8")) or {}).get("favorites") or []
    ACTIVE.mkdir(parents=True, exist_ok=True)
    # Remove previously promoted favorites; hand-made active skills are untouched.
    for d in ACTIVE.iterdir():
        if (d / FAVORITE_MARKER).exists():
            shutil.rmtree(d)
    for ref in wanted:
        cid, _, name = ref.rpartition("/")
        matches = [s for s in skills if s["name"] == name and (not cid or s["collection"] == cid)]
        if not matches:
            print(f"  ! favorite '{ref}' not found")
            continue
        if len(matches) > 1:
            print(f"  ! favorite '{ref}' is ambiguous, using {matches[0]['collection']}/{name}"
                  f" (write it as collection/name)")
        src = REPO / Path(matches[0]["path"]).parent
        dst = ACTIVE / name
        if dst.exists():
            print(f"  ! .claude/skills/{name} already exists (not a favorite), skipped")
            continue
        shutil.copytree(src, dst, ignore=make_ignore([]))
        (dst / FAVORITE_MARKER).write_text(f"{matches[0]['collection']}/{name}\n", encoding="utf-8")
        print(f"  ★ {matches[0]['collection']}/{name}")


def cmd_index() -> None:
    skills = collect_skills()
    write_index(skills)
    write_catalog(skills)
    apply_favorites(skills)
    print(f"Indexed {len(skills)} skills → {INDEX.relative_to(REPO)}, {CATALOG.relative_to(REPO)}")


def main(argv: list[str]) -> int:
    if not argv or argv[0] not in ("sync", "index"):
        print(__doc__)
        return 2
    if argv[0] == "sync":
        cmd_sync(argv[1:])
    else:
        cmd_index()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
