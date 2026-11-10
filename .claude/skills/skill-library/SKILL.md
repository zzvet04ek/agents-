---
name: skill-library
description: Gateway to the project's skill library (hundreds of specialized skills in library/collections/ that are not loaded by default) — framework and language patterns (Django, Spring, Laravel, React, Go, Rust, Kotlin, Swift…), testing/TDD, security reviews, DevOps, databases, agents and LLM pipelines, content and marketing, business operations. Use at the start of any non-trivial task to check whether a specialized skill exists, or when the user names a skill that is not in the active list.
---

# Skill library

The library holds far more skills than can be listed in context, so they live
in `library/collections/<collection>/<skill>/SKILL.md` and are looked up on
demand through `library/INDEX.md`.

## How to use

1. **Search the index — never read it whole.** Each line is
   `name | collection | path | description`. Grep it with 2–4 keywords from
   the task (case-insensitive, alternatives with `|`):
   - `Grep pattern="django|pytest" path="library/INDEX.md" -i`
   - Exact name known: `Grep pattern="^django-tdd \|" path="library/INDEX.md"`
2. **Pick 1–3 best matches** by description. Prefer the more specific skill.
3. **Read the chosen `SKILL.md`** from the path column and follow it as if it
   were an active skill. Files it references (scripts, references/, examples/)
   are relative to that skill's own folder; read them only when needed.
4. Tell the user in one line which library skill you are applying.
5. Nothing fits → proceed normally; don't force a skill.

## Maintenance

- **Add a collection:** copy its skill folders into
  `library/collections/<collection-name>/`, then run
  `python3 library/build_index.py` and commit.
- **Promote a daily-use skill** so it auto-loads: copy its folder into
  `.claude/skills/`. Keep the active set small (well under ~50) — every
  active skill's description costs context in every session.
- Library skills' scripts are third-party code: read before running.
