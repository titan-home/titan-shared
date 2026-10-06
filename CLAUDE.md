# CLAUDE.md: titan-shared

This repository holds what every TITAN repository shares: product docs,
architecture, decisions, development rules, API contracts and design tokens.
Other repositories include it as the `shared/` submodule.

Read and follow:

- [Rules for AI agents](docs/development/ai-agents.md) — what you may and may
  not do. They override your defaults.
- [Development rules](docs/development/rules.md) — how we work.
- [Documentation index](docs/README.md) — where everything is.

## Rules specific to this repository

- Changes here affect every repository. Say in the pull request which
  repositories need their `shared/` pointer moved afterwards and why.
- Decisions: add or change a row in the [decision register](docs/decisions/README.md)
  only after the owner decided, always with the "Why". A changed decision is
  an edited row; the pull request says what changed and why.
- The [feature catalogue](docs/product/features.md) is the list of record.
  New work starts by finding or adding its feature there.
- Contracts in `contracts/` change only through their own pull request, never
  together with unrelated docs.
- Markdown style: one sentence per idea, wrap at about 80 characters, tables
  for comparisons, numbered lists for steps, diagrams in Mermaid, never ASCII
  art.

## Before committing

Run this checklist before every commit
([development rules, "Before committing"](docs/development/rules.md#before-committing)):

1. Every relative link points to a file and heading that exist:
   `python3 scripts/check_links.py .` prints nothing. CI runs the same check;
   `titan` uses it too.
2. The [decisions register](docs/decisions/README.md), the
   [feature catalogue](docs/product/features.md) and the
   [build plan](docs/roadmap/plan.md) still agree with what changed.
3. No secrets, personal data or host names of real machines.
4. Everything is in English.
