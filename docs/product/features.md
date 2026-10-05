# Feature catalogue

A broad catalogue of everything TITAN may do. Two levels: area and feature.
The tag says when a feature is needed: **[v1]** in the first working version,
**[later]** after it, **[?]** an idea the owner still has to accept or drop.
Scenarios and acceptance criteria of the [v1] features live in one file per
area under [domains](domains/), linked from the area's heading.

## 1. Node and platform

Scenarios and acceptance criteria: [node](domains/node.md).

- Install a node on a clean machine with one command [v1]
- Run every service with docker compose [v1]
- Node controller: service health, shown to the owner [v1]
- Update images to pinned versions and roll back a failed update [v1]
- Scheduled database backups and restore from a backup [v1]
- Node configuration and secrets storage [v1]
- nginx as the single entry point, TLS [v1]
- Issue and renew the certificate with `tailscale cert`; other sources later
  [v1]
- Images published by CI; nodes pull them ready-made [v1]
- Service logs and a way to read them [later]
- Metrics: load, response time, errors [later]
- Free disk space check and warning [later]
- Move a node to another machine [later]

## 2. Accounts and access

Scenarios and acceptance criteria: [accounts](domains/accounts.md).

- Create the owner at install time [v1]
- Sign in with username and password [v1]
- Device tokens: pairing the CLI, a browser and the Android app [v1]
- List devices and revoke a device [v1]
- Browser sessions in an HttpOnly cookie [v1]
- Password guessing limited per client address and account [v1]
- Change password [v1]
- Sign out [v1]
- Reset the owner's forgotten password [v1]
- Second factor (TOTP) and recovery codes [later]
- Passkeys [later]
- Household members: create, disable, roles [later]
- Password reset by the owner [later]
- Ask for the password again before dangerous actions [later]

## 3. Chat and agent

Scenarios and acceptance criteria: [chat](domains/chat.md).

- Threads: create, list, rename, delete to a trash kept for 30 days [v1]
- Replies streamed word by word (SSE) [v1]
- A client that reconnects resumes the live reply stream where it stopped
  [later]
- Tool activity visible, with readable translated tool names [v1]
- Approvals inside the reply stream [v1]
- Replies in the language of the message, mixed languages [v1]
- Automatic thread titles [v1]
- Retry when a Claude reply stalls [v1]
- Token usage recorded for every turn [v1]
- Model choice per step: fast and strong [v1]
- The user chooses the models in their settings [later]
- Prompt caching [v1]
- Search across chat history [later]
- Attachments: photos, files, voice messages [?]
- Voice conversation [later]

## 4. Autonomy and trust

Scenarios and acceptance criteria: [autonomy](domains/autonomy.md).

- An action class on every tool: read, write-internal, external, destructive
  [v1]
- Modes auto, auto-undo, confirm, deny [v1]
- A default mode per class, overridden per domain [v1]
- Approvals: Approve and Reject in chat, on the web, on the phone [v1]
- Approvals expire after 24 hours; an expired one counts as rejected [v1]
- An approved call runs exactly as approved, without the agent [v1]
- Audit log with before and after state [v1]
- Undo from the audit log, for one year [v1]
- A monthly warning about actions that are about to lose their undo [v1]
- Browsing the audit log archive [later]
- What the agent sees of health and finance: everything or aggregates only [v1]
- Household-wide default policies [later]

## 5. Tasks and projects

Scenarios and acceptance criteria: [tasks](domains/tasks.md).

- Tasks: title, notes, due date, priority, tags, status [v1]
- Repeating tasks [v1]
- Projects, inbox, archive [v1]
- Filters, saved filters, search, sorting [v1]
- Estimates and links to plan time blocks [v1]
- Table view on wide screens [later]
- Shared projects [later]
- Subtasks [later]

## 6. Calendar and planning

Scenarios and acceptance criteria: [calendar](domains/calendar.md).
The morning plan and replanning a missed block are in
[11. Background workflows](#11-background-workflows).

- Events: one-off, repeating, all-day [v1]
- Time blocks for tasks; a long task is split into several blocks if it can be
  [v1]
- Working hours and days per project, buffer between items [v1]
- Free time lookup [v1]
- Day, week and month views [v1]
- Weekly review [later]
- Inviting members [later]
- iCal import and export [later]

## 7. Reminders

Scenarios and acceptance criteria: [reminders](domains/reminders.md).

- One-off and repeating [v1]
- Fire within 60 seconds, never twice [v1]
- Snooze and Done [v1]
- Default reminders for tasks with a due time and for events [v1]
- Reminder about a pending approval [later]

## 8. Notifications and delivery

Scenarios and acceptance criteria: [notifications](domains/notifications.md).

- Notification history, read and unread [v1]
- Notifications delivered to the Android app over its own connection to the
  node [v1]
- The app catches up on reconnect; nothing is lost or shown twice [v1]
- A bell in the web UI, checked about once a minute [v1]
- Push through ntfy (UnifiedPush) as an option [later]
- Push through Google (FCM) as an option [later]
- Push through Telegram [later]
- Quiet hours, set by the user [later]

## 9. Notes, knowledge and memory

Scenarios and acceptance criteria: [notes](domains/notes.md).

- Markdown notes with tags [v1]
- Word search across notes, tasks and facts, in every script, Chinese and
  Japanese included [v1]
- Search by meaning across languages with a local model [v1]
- Memory: facts about the user the agent learns from chats and notes [v1]
- View, correct and delete facts [v1]
- Agent answers that link to the notes and facts they use [v1]
- Shared notes [later]
- Attachments and images in notes [later]

## 10. Trackers

Scenarios and acceptance criteria: [trackers](domains/trackers.md).

- Templates: habit, weight, sleep, workout, mood, expense, income [v1]
- Custom trackers with a unit and bounds [v1]
- Targets per day, week or month, "at least" or "at most" [v1]
- Logging by a phrase in chat, in any language [v1]
- Streaks and statistics per period [v1]
- Charts [v1]
- Expense and income categories [v1]
- Habit schedule (the days it is due) [v1]
- Import from files (bank, fitness band) [later]

## 11. Background workflows

Scenarios and acceptance criteria: [workflows](domains/workflows.md).

- Morning plan [v1]
- Replanning a missed block [v1]
- Weekly review [later]
- User-defined scheduled workflows [?]

## 12. Claude usage

Scenarios and acceptance criteria: [usage](domains/usage.md).

- A usage screen: tokens and estimated cost per month, by model [v1]
- Monthly cap, warning at 80 %, fast model at 100 % [later]
- Report for the owner across members [later]

## 13. Plugins

Plugins come with build-plan stage 8, after the working version; their
scenarios and acceptance criteria are written then.

- A plugin is a container plus a manifest [later]
- Installed only after the owner approves its manifest [later]
- A plugin token limited to the domains it was granted [later]
- Version pinned by digest; a changed manifest needs a new approval [later]
- Action class never lower than declared; network access at least external
  [later]
- Plugin catalogue [?]
- Plugins on another machine through a TITAN agent that connects to the node
  [later]
- Reversible pseudonymization of confidential plugin data on the plugin's
  machine [later]
- Placeholder table kept on the plugin's machine or on the node, set per plugin
  [later]
- Optional encrypted backup of the placeholder table from the plugin's machine
  to the node, off by default [later]
- External MCP servers [later]

## 14. Clients

Scenarios and acceptance criteria: [clients](domains/clients.md).

- CLI: sign-in, chat, every domain, administration [v1]
- Web: sign-in, chat, node management, every domain [v1]
- Light and dark themes [v1]
- Android, minimal: sign-in, notifications with Snooze, Done, Approve and Reject
  [v1]
- Android, full: chat, today, domains [later]
- Telegram bot [later]
- Voice [later]

## 15. Languages and time

Scenarios and acceptance criteria: [languages](domains/languages.md).

- UI in English, Russian and Ukrainian [v1]
- Any language in data and in chat [v1]
- Time zone from the user's settings [v1]
- Date and number formats from a region setting [v1]

## 16. Household and sharing

- Members and their devices [later]
- Shared projects, notes and events [later]
- Messages to a member through the agent [later]

## 17. Cluster

- Several nodes behind one address [later]
- Data replication [later]
- Choosing the node that runs background work [later]
- Rolling node updates [later]
- A node offline for a week without data loss [later]

## 18. User data

- Export all of one's data [later]
- Delete an account with all its data [later]
- Import from other systems [?]
