# Requirements

The first working version is one node, one user and scenarios 1–7 from the
[vision](vision.md). Household, budget and cluster come later, but decisions
made now must not rule them out.

## Per domain

What each area does in the working version is in its spec under
[domains](domains/); this table says only what is deferred.

| Area | Spec | Deferred |
|---|---|---|
| Node and platform | [node](domains/node.md) | Service logs, metrics, disk space warning, moving a node, cluster |
| Accounts and access | [accounts](domains/accounts.md) | Second factor (TOTP) and recovery codes, passkeys, household members, password reset by the owner, re-asking the password before dangerous actions |
| Chat and agent | [chat](domains/chat.md) | Resuming a live stream after reconnecting, choosing models in settings, search across chat history, attachments, voice |
| Autonomy and trust | [autonomy](domains/autonomy.md) | Browsing the audit log archive, household-wide default policies |
| Tasks and projects | [tasks](domains/tasks.md) | Table view on wide screens, shared projects, subtasks |
| Calendar and planning | [calendar](domains/calendar.md) | Weekly review, inviting members, iCal import and export |
| Reminders | [reminders](domains/reminders.md) | Reminder about a pending approval |
| Notifications and delivery | [notifications](domains/notifications.md) | ntfy and FCM as push options, Telegram, quiet hours |
| Notes, knowledge and memory | [notes](domains/notes.md) | Shared notes, attachments and images in notes |
| Trackers | [trackers](domains/trackers.md) | Import from files |
| Background workflows | [workflows](domains/workflows.md) | Weekly review, user-defined scheduled workflows |
| Claude usage | [usage](domains/usage.md) | Monthly cap and warnings, report across members |
| Clients | [clients](domains/clients.md) | The full Android app (chat, today, domains), Telegram bot, voice |
| Languages and time | [languages](domains/languages.md) | — |
| Plugins | — | All of it: build-plan stage 8 and later |

## Cross-cutting

- **Own infrastructure.** Runs on your machines: one computer or a cluster.
  Access is not hard-wired: the owner uses Tailscale, but any private
  network, VPN or proxy with TLS works. Only requests to Claude leave the
  node.
- **The agent works only through tools.** It has no shell, no files and no
  direct database access.
- **Private by default.** Multi-user from day one even with one user: every
  record has an owner and nobody sees other people's data. In background
  workflows the agent sees health and finance only as aggregates, without
  single entries.
- **Languages.** The agent replies in the language of the message and
  understands mixed languages. Nothing is tied to a list of languages:
  Chinese and Japanese must work too, including search (they have no spaces
  between words) and parsing of dates and amounts. The UI is translated into
  English, Russian and Ukrainian first. Data is stored in the language it was
  written in.
- **Time.** Everything is computed in the time zone the user set in their
  settings, not the server's or the browser's; "every day at 9:00" stays at
  9:00 across daylight saving changes.
- **Security.** Passwords are hashed, every device has its own revocable
  token, password guessing is limited per client address and account. In the
  browser no script can read the token.
- **Connectivity.** Clients are online-only, but losing the connection never
  clears what is on screen; writes are never queued.
- **Cost.** A fast, cheap model for simple steps, a strong one for
  conversation and planning; prompt caching. The owner's Claude subscription
  is used; its limits are shared with the owner's own Claude Code use.
