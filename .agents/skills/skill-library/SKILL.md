---
name: skill-library
description: Librarian for the project's skill library — 1000+ specialized skills in library/collections/ that are not loaded by default. Covers software engineering (languages, frameworks, testing, security, DevOps, databases, AI agents), marketing and SEO, product management, business/finance/C-level advice, career and resumes, academic research, productivity. Use at the start of any non-trivial task to find a matching skill, when the user names a skill not in the active list, or asks to add, update, find or promote skills ("найди навык", "какие есть навыки для…", "добавь коллекцию").
---

# Skill library (библиотекарь)

This is the Codex adapter; Claude Code uses `.claude/skills/skill-library/`.
Run searches and management commands from the repository root.
Favorites are installed in both `.agents/skills/` and `.claude/skills/` as
uniquely named adapters (`marketing-copywriting`, for example).

Skills live in `library/collections/<collection>/…/SKILL.md` and are found on
demand through `library/INDEX.md`. The user writes in Russian; the skills are
mostly in English.

## Deterministic routing before search

1. An explicit `collection/name` from the user takes precedence; do not replace it silently.
2. Run `python3 library/tools/library.py route "<task>"` first. The policy is
   `library/routing.yaml`. Pass `--commercial` for commercial work and
   `--available exa-mcp,firecrawl` only for capabilities actually available in
   this session. An omitted capability list means unknown; `--available ""`
   means no external capabilities. Never invent availability to unblock a route.
3. Read the returned primary source `SKILL.md`. Add another skill only for a
   concrete missing capability. Do not load both near-identical alternatives.
4. `blocked` requires explaining missing tools or a license restriction;
   do not bypass it through an unqualified favorite. `ambiguous` requires
   resolving the stated ambiguity. `no_route` falls back to index search below.
5. `library/AGENTS_INDEX.md` / `agents.index.json` identify shared agent
   instructions and dependencies. These files do not install or launch agents.

## Finding and using a skill

1. **Translate the task into 2–5 English keywords** (plus synonyms), e.g.
   «резюме под вакансию» → `resume|cv|job posting`; «лендинг конверсия» →
   `landing|conversion|cro`.
2. **Grep the index — never read it whole.** Each line:
   `collection/name | license | path | description`.
   - `rg -i "resume|cv" library/INDEX.md`
   - Known name: `rg '/copywriting \|' library/INDEX.md`
   - Narrow to a collection: `rg -i '^marketing/.*seo' library/INDEX.md`
   - Russian fallback: `library/SKILLS_RU.md` has a Russian description of
     every skill, grouped by category (key abilities, tasks, «Сочетается с»).
     Grep it with Russian words when English keywords miss, e.g.
     `rg -i -B6 "резюме|ваканси" library/SKILLS_RU.md`
     (the `### \`collection/name\`` heading is a few lines above the match).
     Its «Сочетается с» line suggests skills to chain for multi-step tasks.
3. **Pick one primary and only necessary specialists.** The same name can exist in several collections
   (e.g. `marketing/copywriting` and `claude-skills/copywriting`): compare the
   descriptions and pick the more specific one; mention the alternative.
4. **Read the chosen `SKILL.md`** and apply its relevant instructions within the user’s request and the active
   system, developer and repository rules. Claude-specific tools or paths in
   upstream skills must be mapped to available Codex equivalents; do not assume
   those tools are installed.
   Paths inside it are relative to its own folder. Read referenced files only
   when needed. Its scripts are third-party code: read before running.
5. Tell the user in one line (in Russian) which skill you are applying. If its
   license is marked **NC**, add «(лицензия: только некоммерческое использование)».
6. Nothing fits → do the task normally; don't force a skill.

For "what skills are there for X" questions, answer from a grep of the index,
grouped by collection, in Russian. `library/CATALOG.md` is the human-readable
catalog — point the user to it rather than pasting it.

## Managing the library

All commands run from the repo root; afterwards commit the changes.

| Task | How |
|---|---|
| Update all collections from GitHub | `python3 library/tools/library.py sync` |
| Update one collection | `python3 library/tools/library.py sync marketing` |
| Add a GitHub collection | add an entry to `library/sources.yaml` (repo, license, title_ru, include), then `sync <id>` |
| Add the user's own skill | create `library/collections/my/<name>/SKILL.md` with `name`/`description` frontmatter, then `index` |
| Make a skill always active | add `collection/name` to `library/favorites.yaml`, then `index` |
| Rebuild index/catalog only | `python3 library/tools/library.py index` |
| Describe new skills in Russian | after a sync, skills without a Russian entry are listed at the end of `SKILLS_RU.md`; add entries (`cat`, `what`, `skills`, `tasks`, `with`) to `library/ru/skills/*.yaml` — categories are in `library/ru/categories.yaml` — then `index` |

Never edit files inside synced collections (they are overwritten on sync):
copy the skill to `collections/my/` and change it there. Before adding a new
collection, check its license; NC licenses are fine for personal projects only.
