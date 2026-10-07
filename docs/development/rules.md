# Development rules

These rules apply to every TITAN repository, for people and AI agents alike.
They are deliberately broad; the owner trims and corrects them over time. A
repository may add rules of its own in its `CLAUDE.md` and `docs/`, but may
not contradict these. Rules for AI agents in particular are in
[ai-agents.md](ai-agents.md).

## 1. Principles

1. **The owner decides.** Every significant choice is the owner's. Options are
   prepared with their trade-offs; a decision is recorded only once the owner
   has made it.
2. **Understanding before speed.** A change the owner cannot explain is not
   done. Prefer a slower step the owner understands to a faster one they do
   not.
3. **Small steps.** One change at a time, each one working and reviewable on
   its own.
4. **Working software at every step.** Every stage ends with something that
   runs; nothing stays half-built on the main branch.
5. **Simple and boring.** The least code, the fewest moving parts, the most
   ordinary technology that does the job. No abstraction without a second
   real use, no configuration for a value that never changes, nothing built
   "for later". A clear seam, a separate function or module with one
   implementation, is not an abstraction; an interface, a registry or a
   plugin system for one implementation is.
6. **Documents first.** Work flows from the documents to the code, never the
   other way round.
7. **Private and safe by default.** Every record has an owner; nothing is
   shared, exposed or logged unless a rule says so.

## 2. Workflow

Every piece of work goes through the same steps:

1. **Feature.** Find it in the [feature catalogue](../product/features.md). If
   it is missing, add it there first.
2. **Spec.** Describe what it does: behaviour, edge cases, acceptance
   criteria. Product behaviour lives in `titan-shared/docs/product/domains/`,
   one file per area: a scenario, numbered acceptance criteria and open
   questions. Details that concern one repository live in that repository's
   `docs/`.
3. **Decide.** If the work needs a significant or hard-to-reverse choice,
   bring the options to the owner and record the decision, with why, as a
   row in the [decision register](../decisions/README.md).
4. **Plan.** Break the work into steps small enough to review, in the
   [build plan](../roadmap/plan.md) or a plan of its own under
   `docs/roadmap/`.
5. **Implement.** Scaffolding and tests first, then the key part (often
   written by the owner), then review.
6. **Document.** Update the permanent docs in the same pull request as the
   change. When a stage is finished, delete its plan.

A bug fix may skip steps 1–4 when the expected behaviour is already in a spec;
it still needs a test that fails without the fix.

## 3. Documentation

- **Language.** All documentation, code, comments, commit messages and pull
  requests are in English. Chat with the owner is in the owner's language.
- **Where things live.**

  | Kind | Place | Lifetime |
  |---|---|---|
  | Product: vision, requirements, feature catalogue | `titan-shared/docs/product/` | Permanent |
  | Domain specs: scenarios and acceptance criteria, one file per area | `titan-shared/docs/product/domains/` | Permanent |
  | Architecture shared by several repositories | `titan-shared/docs/architecture/` | Permanent |
  | Decisions of every repository, with why | `titan-shared/docs/decisions/README.md` | Permanent; a changed decision is an edited row, history in git |
  | Development rules | `titan-shared/docs/development/` | Permanent |
  | API contracts | `titan-shared/contracts/` | Permanent, versioned |
  | Design tokens | `titan-shared/design/` | Permanent, versioned |
  | One repository's architecture and notes | that repository's `docs/` | Permanent |
  | Plans and task lists | `docs/roadmap/` | Volatile; deleted when done |

- Never keep lasting knowledge only in a plan; never put plans outside
  `docs/roadmap/`.
- Docs describe how things are now. Why a choice was made lives in the
  decision register; docs link to its row instead of repeating it.
- **Style.** Write for a person reading for the first time. Lead with the
  point. Short sentences, plain words, concrete numbers and names. Tables for
  things compared on several attributes, numbered lists for steps, diagrams
  for flows and structures. No filler, no marketing tone.
- **Diagrams** are [Mermaid](https://mermaid.js.org/) blocks in the Markdown,
  never ASCII art: GitHub renders them, and they stay text that is easy to
  edit and review.
- **Every repository has** `README.md` (what it is, how to run it),
  `CLAUDE.md` (rules for AI agents in this repository) and `LICENSE`.
  `titan-node`, `titan-backend`, `titan-web` and `titan-android` also have
  the `shared/` submodule; `titan` and `titan-shared` do not.

## 4. Repositories and the shared submodule

- Repositories: `titan`, `titan-shared`, `titan-node`, `titan-backend`,
  `titan-web`, `titan-android`, and later `titan-agent`. Each one builds,
  tests and releases on its own.
- All repositories are public on GitHub, in the organization
  [`titan-home`](https://github.com/titan-home); images are published to
  `ghcr.io/titan-home/`. Nothing that must stay private belongs in any of
  them.
- `titan-shared` is attached as a git submodule at `shared/` to `titan-node`,
  `titan-backend`, `titan-web` and `titan-android`. The releases repository
  `titan` holds only manifests and release notes and links to the shared docs
  on GitHub.
- **Never edit files under `shared/` from another repository.** Change
  `titan-shared` through its own pull request, then move the submodule pointer
  in the repositories that need it, in their own pull requests.
- A pull request that moves the `shared/` pointer says which shared commits it
  takes in and what changes because of them.
- Clone with `git clone --recurse-submodules`; after a pull, run
  `git submodule update --init`.
- CI checks out submodules and fails if `shared/` points to a commit that is
  not on `titan-shared`'s main branch.

## 5. Git

- **Main branch:** `master`. It always builds and passes its checks. Nobody
  pushes to it directly; every change arrives through a pull request.
- **Branch names:** `<kind>/<stage>-<topic>`, lowercase kebab-case, at most
  50 characters. Kind is `feature`, `fix`, `docs`, `refactor`, `chore`,
  `research` or `spike`. Stage is the build-plan stage, `s0`–`s8`, or `later`.
  Example: `feature/s2-create-task-tool`. A change that spans repositories
  uses the same branch name in each of them.
- **Commits:** small, each one building and passing tests on its own.
  - Title: a past-tense verb first (`Added …`, `Fixed …`, `Removed …`), at most
    72 characters, no trailing period, no `feat:`-style prefixes, no issue
    numbers.
  - Body: one plain paragraph on what changed and why, wrapped at 72.
  - No AI attribution: no `Co-Authored-By` or session trailers.
  - Dependabot's commits keep the titles it writes, `Bump … from … to …`,
    since it cannot be told to use another verb
    ([decision #95](../decisions/README.md#register)).
- **History:** `master` has a linear history. Pull requests are merged by
  rebase, so every commit lands on `master` as it is and must stand on its
  own.
  - Inside a branch, history may be rewritten freely before the merge:
    reorder, squash fix-ups, split or reword commits, so that the branch tells
    a clean story when it lands. Force-pushing a branch is allowed, with
    `--force-with-lease`.
  - `master` is never rewritten and never force-pushed.
- **Tags:** releases are tagged `v<major>.<minor>.<patch>`.
- Never commit generated files that the build can produce, secrets, `.env`
  files, local editor settings or personal data.

## 6. Pull requests

- **Size:** one logical change, small enough to review in one sitting. Split
  anything bigger.
- **Title:** the same rules as a commit title.
- **Description:** what changed, why, how to verify it, risks, links to the
  feature, spec or decision. No AI attribution or "Generated with" footers.
- **Before review:** formatted, linted, type-checked, tests pass locally, docs
  updated, no debugging leftovers.
- **Review:** the owner reviews and merges. AI may review and comment but
  never merges. Every comment is either resolved by a change or answered.
- **CI must be green** before merging. A check is never disabled to get a
  merge through; a flaky check is fixed or removed in its own pull request.

## 7. Code

### General

- Code reads like the code around it: same naming, idioms and comment density.
- Names say what a thing is or does, in full words.
- Comments explain *why*, not *what*. Every public function, class and module
  has a one-line doc comment saying what it is for.
- No dead code, commented-out code or unused parameters.
- Validate input at trust boundaries (API, CLI, plugin, file, environment);
  trust our own types inside.
- Handle errors where something useful can be done; otherwise let them
  surface. Never swallow an error silently.
- Prefer the standard library, then an already-used dependency, then a new
  dependency (see section 13).
- A deliberate shortcut with a known limit is marked with a comment that
  starts with `NOTE:` and names the limit, then the way out, for example
  `# NOTE: scans every open task, fine up to a few thousand; index on due
  date when slow`. `grep NOTE:` then lists every such shortcut.

### Python (`titan-backend`)

- Python 3.12 or newer, managed with `uv`; dependencies and their lock file in
  `pyproject.toml` and `uv.lock`.
- `ruff format` and `ruff check`; `mypy --strict`; `pytest`.
- Async I/O throughout the API and worker; no blocking calls on the event loop.
- Layering is enforced: domains never import the API or the agent layer.
- Data the audit log covers (`Audited` models) is changed only through ORM
  objects, never with bulk `update`, `insert` or `delete` statements, which
  the log does not see ([decision #110](../decisions/README.md#register)).

### TypeScript (`titan-web`)

- TypeScript in strict mode; ESLint with zero warnings; Prettier.
- The API client is generated from the contract in `shared/contracts/`; never
  edit generated code.
- Every user-visible string goes through the translation layer.

### Go (`titan-node`)

- The Go version pinned in `go.mod`; `gofmt`, `go vet`, `golangci-lint`.
- Errors are wrapped with context and returned, never ignored; no panics
  outside `main`.
- `context.Context` on every call that does I/O.

### Kotlin (`titan-android`)

- Kotlin with Jetpack Compose; ktlint; the API client generated from the
  contract.

## 8. Testing

- **Tests come with the change they cover**, in the same pull request.
- **A bug fix starts with a test that fails** without the fix.
- **Every acceptance criterion** in a domain spec has at least one test that
  names it, so a spec and its tests cannot drift apart unnoticed.
- **Real dependencies where it matters:** database tests run against real
  PostgreSQL, not mocks; end-to-end tests run the real build in real browsers
  under the real security headers.
- **Deterministic:** no real clock, network or randomness in unit tests; time
  is injected. A flaky test is fixed or deleted, never retried until green.
- **Levels:**

  | Level | What | Where |
  |---|---|---|
  | Unit | Pure logic, parsing, policy decisions | Every repository |
  | Integration | API with a real database, a tool with its domain | `titan-backend` |
  | Contract | The API matches the contract in `shared/contracts/` | `titan-backend`, clients |
  | End-to-end | The built UI in Chromium, Firefox and WebKit under the CSP; where Playwright's own browsers do not start, in the Playwright container or with the system browser | `titan-web` |
  | Node | Install, update, rollback and restore on a clean machine, with a self-signed certificate | `titan-node` |

- **Everything automatic runs on GitHub-hosted runners**, node tests
  included: a job is a clean machine with Docker. Nothing runs on the
  owner's machines automatically ([decision #82](../decisions/README.md#register)).
  Before a release the owner checks by hand what CI cannot: a real
  `tailscale cert` and the reference machine's resources.

- Agent behaviour is tested with recorded or scripted model replies; the
  regular tests never call the real Claude API.
- **Live tests** are a separate group that talks to the real Claude with the
  owner's OAuth token or API key, to check what scripted replies cannot. They
  are run **only by the owner**, by hand: never in CI, never by an AI agent,
  never as part of the pre-commit checklist. They are skipped unless the owner
  explicitly selects them and provides the credential.

### Before committing

Every repository keeps a separate **pre-commit checklist** in its `CLAUDE.md`,
under "Before committing": the checks that must pass before every commit.

- It is a short, fast subset, not the whole test suite: formatting, linting,
  type checks, the tests of the code the commit touches, and the extra checks
  a kind of change calls for (a migration, a contract change, a new library).
- The full suite runs in CI on every pull request; the checklist exists so
  that a commit is not broken on arrival.
- Everyone runs it before committing, people and AI agents alike. A check that
  cannot run (a missing tool, a service that is down) is reported, never
  silently skipped.
- The checklist changes like any rule: through a pull request the owner
  approves.

## 9. API and contracts

- The API contract (OpenAPI) lives in `titan-shared/contracts/` and is the
  source of truth for every client. The backend checks in CI that it serves
  exactly that contract.
- Paths are versioned: `/api/v1/…`. Within a version, changes are additive
  only; removing or changing a field needs a new version or an
  expand-and-contract migration across releases.
- Errors use `application/problem+json` (RFC 9457) with a stable `type`.
- Ids are UUIDs. Timestamps are ISO 8601 in UTC with an offset; local dates
  and times are sent with their time zone name.
- Lists are paged: the client asks for a page size with `limit`, and the node
  caps it at a maximum set in the node's configuration, 100 by default. The
  contract documents the default; a client never assumes more
  ([decision #83](../decisions/README.md#register)).
- Anything another user cannot see answers `404`, as if it did not exist.
- Streaming uses server-sent events; nginx must not buffer them, and an
  end-to-end test checks the stream through the real nginx config.
- Internal links in reply text use the `titan://` scheme, defined in the
  contract ([decision #74](../decisions/README.md#register)).

## 10. Data and migrations

- Every user-owned table has an owner column, and every query filters by it in
  the service layer.
- Primary keys are UUIDs, generated by the application. A record created by
  a background event, such as a notification from a reminder, gets an id
  derived from its cause, so firing twice cannot create a duplicate.
- Timestamps are `timestamptz`; money and measured values are exact decimals.
- Schema changes are migrations in the repository that owns the database
  (`titan-backend`). Migrations are forward-only and reviewed like code.
- Destructive changes use expand and contract: add the new shape, migrate,
  switch readers, then remove the old shape in a later release.
- Items that go to the trash are marked deleted, with the time, and are
  excluded by every query by default; the worker removes them for good after
  30 days ([decision #31](../decisions/README.md#register)).
- The controller takes a backup before every update that migrates the
  database.

## 11. Security

- **Secrets** never enter git, logs, error messages, issue trackers or chat.
  They live in the node's secret store, managed by the controller
  ([decision #77](../decisions/README.md#register)).
- **Least privilege:** containers run as non-root users with read-only file
  systems where possible; only nginx is reachable from outside the node; the
  controller's Docker access is the most sensitive privilege on the node and
  is guarded accordingly.
- **Authentication:** passwords hashed with Argon2id; device tokens stored only
  as hashes; browser sessions in `HttpOnly`, `Secure`, `SameSite=Lax`
  cookies, and every request other than `GET` or `HEAD` with a foreign
  `Origin` is refused ([decision #26](../decisions/README.md#register));
  password guessing limited per client address and account, never the
  account alone; the client address is taken from `X-Forwarded-For` only
  when the request comes from one of our own proxies.
- **Authorization** is checked in the service layer on every access, never only
  in the client.
- **Web:** a strict Content-Security-Policy, Trusted Types, no inline scripts,
  no third-party assets; server text is never rendered as raw HTML. Every new
  library is checked with an end-to-end test under the CSP, because
  libraries that use inline scripts or `data:` URLs break under it.
- **Supply chain:** lock files committed; CI actions pinned to commit hashes;
  images pinned by digest; new dependency versions wait 14 days after release
  before the update bot proposes them, security fixes excepted.
- **Logs** never contain passwords, tokens, message contents, search text or
  other personal data; query parameters are never logged, since search text
  travels in them.
- A security problem found in review is fixed before anything else is merged.

## 12. Privacy

- All data belongs to one user and is private by default; sharing is explicit
  and per item or collection.
- Health and finance data reach background workflows only as aggregates,
  unless the user allows more.
- The notification stream to our own app may carry the content; a push through
  any third-party service carries only an id, and the content is fetched over
  the API.
- Users can export and delete all of their data (later stage).

## 13. Dependencies

- Every new dependency needs a reason in its pull request: what it does that a
  few lines of our own code or an existing dependency cannot.
- Licences must be permissive and compatible with releasing TITAN under the
  Unlicense. The one exception is the Claude Code binary bundled with the
  Agent SDK, used unmodified under Anthropic's terms
  ([decision #100](../decisions/README.md#register)).
- Prefer widely used, maintained projects. Pin versions through lock files.
- Updates arrive as their own pull requests and pass every check.

## 14. Agent and tools

- The agent reaches data only through tools. It has no shell, file system or
  database access.
- Every tool declares: a name, a description the model reads, an action class
  (`read`, `write-internal`, `external`, `destructive`), an input schema, a
  one-line summary a person can approve, and, where possible, how to undo it.
- A tool checks the caller's access like any API endpoint.
- Tools are idempotent where they can be; a retried call does not duplicate.
- A tool without an undo is never run in `auto-undo`; it is treated as
  `confirm` ([decision #37](../decisions/README.md#register)).
- Every tool call is written to the audit log.
- Every tool has tests, including access checks and its undo.
- Policy is enforced in the tool hooks of the agent runtime, never by the
  prompt alone, so the agent cannot bypass it; an approved call runs later
  without the agent, exactly as approved.
- The Agent SDK runs with a clean environment that holds exactly one
  credential, the subscription's OAuth token, and its session transcripts go
  to tmpfs. `ANTHROPIC_API_KEY` in the environment takes precedence over the
  OAuth token and silently switches every call to API billing, so the api and
  worker start the SDK with an environment built from scratch, never
  inherited, and a test asserts that no `ANTHROPIC_*` variable reaches it.
  Transcripts on disk would hold conversations.
- Prompt changes are reviewed like code and covered by scripted tests.
- Plugins follow the same rules and the [plugin trust rules](../decisions/README.md#plugin-trust-9).

## 15. Languages and time

- Nothing assumes one language or script: search, parsing and sorting work for
  any language, including Chinese and Japanese.
- Stored text stays in the language it was written in.
- Clients translate every user-visible string; English, Russian and Ukrainian
  first.
- Date, time and number formats follow the user's region setting, separate
  from the UI language ([decision #75](../decisions/README.md#register)).
- All times are computed in the time zone from the user's settings. Repeating
  items keep their local time across daylight saving changes.
- Each client has one shared date helper, tested with several time zones,
  all-day items and daylight saving changes; no screen does its own date
  arithmetic.

## 16. Errors, logging and observability

- Logs are structured (one JSON object per line), with a request id that
  follows a request through every service.
- Errors shown to users are short and actionable; details go to the log.
- Every service has a health endpoint that the controller checks.

## 17. CI and releases

- Every repository runs its checks on every pull request: format, lint, types,
  tests, build. Image builds run too.
- Images are built and published by CI on a version tag, never on a laptop;
  nodes pull them ready-made and never build from source. The API and the
  worker are separate images, so a node shows what each one runs.
- A TITAN release is a manifest in the `titan` repository that pins every
  component by version, source commit and image digest; see its `CLAUDE.md`.
- Versions follow SemVer. Each release has notes: what changed for the user,
  what changed for operators, any migration.
- Compatibility between components (UI, API, controller) is stated in each
  release's notes.

## 18. Clients and UX

- Losing the connection never clears data on screen and never shows a
  full-page spinner; writes are disabled or fail with a short message, never
  queued.
- Actions that cannot be undone ask for confirmation: deleting for good,
  emptying the trash. Moving to the trash does not ask; it shows an Undo for
  a few seconds instead ([decision #84](../decisions/README.md#register)).
- Keyboard navigation, screen reader labels and sufficient contrast on every
  screen.
- Light and dark themes.

## 19. Resources

- The reference test machine is a virtual machine with 2 CPU cores and 8 GB of
  memory; a node must run comfortably on it, and anything that needs more is
  optional.
- Real nodes have somewhat more resources but share them with other services,
  so TITAN keeps a modest footprint: bounded memory per container, no busy
  polling, and heavy work (embeddings, backups) scheduled and throttled.
