# Build plan

The working version is the end of stage 7: scenarios 1–7 work through the CLI,
the web and a minimal Android app on one node. Every stage ends with something you can run and
touch. Stages go one at a time; there is no fixed rhythm, and steps are as small
as makes sense.

## How every step goes

1. AI brings the step's forks with options; the owner decides.
2. The decision, with why, becomes a row in the decision register in
   `titan-shared`; the spec describes the result.
3. AI prepares the scaffolding and the tests; the owner writes the key part;
   AI explains and reviews.
4. One small pull request; the owner merges it.

## Stages

| # | Stage | What works at the end | Owner's forks | Owner's code |
|---|---|---|---|---|
| 0 | Foundation | Repositories `titan-shared`, `titan-backend`, `titan-node`, `titan-web`, `titan` with green CI; shared attached as a submodule; development rules agreed | Licence (done: Unlicense); branch, commit and review rules; what AI may and may not do | The development rules, together |
| 1 | Backend skeleton | `docker compose up` starts api and PostgreSQL; the owner is created by a command; `titan login` and `titan whoami` work | Decided: packaging (#85), database access and migrations (#86), contract source (#87), CLI (#88, #89), sign-in path (#90), signing in again (#91), error types (#92); the device token format was settled earlier (#29) | User model and sign-in |
| 2 | Agent end to end | `titan chat "add a task to buy milk"`: the reply streams, the task is in the database. Chat-turn graph in LangGraph, Agent SDK with the subscription, one tool | How chat history is stored; the system prompt; how a tool is described | The first tool, `create_task` |
| 3 | Policy and audit log | 4 classes, a default mode per class with per-domain overrides; a dangerous action waits for `titan approve`; the log with undo | Audit entry format; what "undo" means for each tool | The policy hook |
| 4 | Node | `titan-node` installs and updates a node: Go controller (health, images by digest, rollback, backups, secrets), nginx with TLS; images published by CI | Decided in advance: certificate source (#18), secrets (#77), controller protection (#78) | The controller — the owner's first Go project |
| 5 | Web: sign-in, chat, node management | In the browser: password sign-in, chat with approvals, node health, updates and backups; CI refuses a change to the `/api/v1` contract that is not additive | Visual style; which management features come first | The node management screen |
| 6 | Domains | One at a time, in the CLI and the web: tasks → reminders and the notification stream → calendar and daily plan → trackers → notes, memory and local embeddings | Each domain's data model; its tools' classes | At least one tool in every domain |
| 7 | Minimal Android app | Sign-in, the notification stream over the app's own connection, notifications with Snooze, Done, Approve and Reject (decisions #14, #23). **Working version.** | How the app keeps its connection and catches up; what the first screen shows | The notification service |
| 8 | Plugins | Manifest, container run by the controller, token for granted domains, install with approval; the first plugin works | Manifest format; which permissions a plugin may ask for | The first plugin — one the owner needs |

## Later, in any order

The full Android app (chat, today, domains), Telegram bot, household and sharing, Claude budget, second factor
(TOTP), the `titan-agent` for plugins on other machines (decisions #21, #22,
#80, #81), external MCP servers, voice, cluster and replication.

