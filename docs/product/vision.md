# Product vision

TITAN is a personal AI assistant that lives on your own machines and keeps
track of everything that matters to a person or a household: tasks, time,
notes, habits, health and money. It plans your day with you, reminds you at
the right moment and remembers what you told it. No data leaves your machines
except the requests to the Claude model.

## Principles

- **A daily tool, not a playground.** At every fork, choose what gives
  reliable daily use sooner, not what is more interesting to build.
- **The owner understands the system.** The owner makes the decisions and
  writes the key code; AI prepares options, scaffolding, tests and reviews.
- **Your own machines.** One machine or a cluster. Access is not hard-wired:
  Tailscale, any private network, a VPN or a proxy with TLS.

## Users

| Role | Can do |
|---|---|
| Owner | Everything a member can, plus nodes, accounts, the Claude credential, budgets, default policies and plugins |
| Member | Use the assistant, own their data, share it explicitly, set their own autonomy |

Today there is one user, the owner. A household may come later, so the system
is multi-user from day one: every record has an owner and access checks are
real.

## Scenarios

| # | Scenario | What it looks like | When |
|---|---|---|---|
| 1 | Reminder from chat | You write in any language "remind me tomorrow at 9 to buy milk"; at 9:00 the phone shows the reminder with Snooze and Done | Now |
| 2 | Tasks and projects | Tasks with due dates, priorities and repeats; the agent creates and completes them when asked | Now |
| 3 | Daily plan | In the morning a plan arrives: calendar events and time blocks for tasks; the agent moves a missed block | Now |
| 4 | Trackers | "Spent 23.40 on groceries", "slept 7 hours" → a tracker entry; habit streaks and charts per week or month | Now |
| 5 | Notes and memory | "What did I note about the car service?" finds the note, even in another language; the agent remembers facts about you | Now |
| 6 | Approvals | The agent does dangerous things only after your Approve in chat, on the web or on the phone | Now |
| 7 | Audit log and undo | Everything the agent did is in the log; much of it can be undone with one tap | Now |
| 8 | Household | Several accounts, shared projects and notes, event invitations | Later |
| 9 | Claude budget | Tokens and cost per person, a monthly cap with a warning | Later |
| 10 | Cluster | Several nodes; a laptop goes offline for a week, everything keeps working on the others, a reminder fires exactly once | Later |
| 11 | Voice | Talk to the assistant and hear the answer | Later |

## Non-goals

- Public hosting for other people.
- Google Calendar, email and bank integrations in the first version (later
  through plugins).
- iOS and desktop apps.
