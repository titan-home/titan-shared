# Autonomy and trust

What the agent may do on its own, what waits for the user, and how every
action can be traced and undone.
This file deepens area 4 of the [feature catalogue](../features.md) into
scenarios and acceptance criteria.
Only [v1] features are described; the rest stay in the catalogue.

## An action class on every tool: read, write-internal, external, destructive [v1]

Every tool says how risky it is, so the policy can treat it accordingly.

**Acceptance criteria**

1. Every tool declares exactly one class: `read`, `write-internal`,
   `external` or `destructive`.
2. A tool without a class cannot be registered.
3. A plugin's tool class can only be raised by the node, never lowered; a
   plugin tool with network access is at least `external`
   ([plugin trust](../../decisions/README.md#plugin-trust-9)).

## Modes auto, auto-undo, confirm, deny [v1]

The mode says what happens when the agent calls a tool.

**Acceptance criteria**

1. `auto`: the call runs; it shows only in the audit log.
2. `auto-undo`: the call runs at once, and the reply shows it with an Undo
   button ([decision #37](../../decisions/README.md#register)).
3. A tool without an undo is never run in `auto-undo`; it is treated as
   `confirm`.
4. `confirm`: the call does not run; it becomes an
   [approval request](#approvals-approve-and-reject-in-chat-on-the-web-on-the-phone-v1).
5. `deny`: the call does not run, and the agent is told it is not allowed.

## A default mode per class, overridden per domain [v1]

Sensible defaults work out of the box; the user tightens or loosens a class
only where a domain needs it.

**Acceptance criteria**

1. The defaults are ([decision #38](../../decisions/README.md#register)):

   | Class | Default mode |
   |---|---|
   | `read` | `auto` |
   | `write-internal` | `auto-undo` |
   | `external` | `confirm` |
   | `destructive` | `confirm` |

2. Each user can set a different mode for one class in one domain, for
   example `confirm` for `write-internal` in finance
   ([decision #10](../../decisions/README.md#register)).
3. A user's settings apply only to that user's agent.
4. No class defaults to `deny`; it is only ever set by hand.

## Approvals: Approve and Reject in chat, on the web, on the phone [v1]

An action that needs approval waits until the user decides, wherever they
are.

**Acceptance criteria**

1. The request shows the tool's one-line summary, its domain and its class.
2. It can be decided in the chat, on the web, or from the notification in
   the Android app ([decision #23](../../decisions/README.md#register)).
3. A request is decided once; a second Approve or Reject, from any device,
   changes nothing.
4. Only the user whose agent made the request sees and decides it; anyone
   else gets `404`.

## Approvals expire after 24 hours; an expired one counts as rejected [v1]

**Acceptance criteria**

1. A request not decided within 24 hours expires and counts as rejected.
2. An expired or rejected request never runs, and the audit log keeps a
   record of it.

## An approved call runs exactly as approved, without the agent [v1]

What the user approved is what runs, even a day later.

**Acceptance criteria**

1. The request stores everything that was approved: the tool, its input,
   its class and the data it may expose.
2. On Approve the node runs exactly that call, without asking the agent
   again.
3. The result is added to the thread as a message; the agent sees it with
   the user's next message ([decision #39](../../decisions/README.md#register)).

## Audit log with before and after state [v1]

Everything the agent did can be looked up afterwards.

**Acceptance criteria**

1. Every tool call is written to the log, built-in and plugin calls alike:
   when, which tool, its class and mode, the input, the outcome, and the
   fields it changed, before and after
   ([decision #108](../../decisions/README.md#register)).
2. Calls that did not run, rejected, expired or denied, are in the log too.
3. A user sees only their own log.
4. Entries are kept for good, except that when an object is deleted for
   good, its entries are erased with it ([decision #41](../../decisions/README.md#register)).
5. Entries older than one year are moved to an archive where they are
   stored as compactly as possible; they are kept, but can no longer be
   undone. Browsing the archive comes later.

## Undo from the audit log [v1]

Much of what the agent did can be undone with one tap.

**Acceptance criteria**

1. An action can be undone from its log entry for one year, while the entry
   is in the main log and not yet in the archive
   ([decision #40](../../decisions/README.md#register)).
2. If the record changed after the action, the undo is refused with a short
   explanation; it never overwrites a later change.
3. An undo is itself written to the log.
4. Undoing puts back what the action changed: old values return, a created
   item moves to the trash, a deleted one comes back from it
   ([decision #109](../../decisions/README.md#register)).
5. An action that changed several items is undone whole; if any of them
   changed after the action, the whole undo is refused.

## Warning before actions go to the archive [v1]

An action never loses its undo without the user having had a chance to see
it.

**Acceptance criteria**

1. Once a month the user gets a notification about the agent's actions that
   move to the archive within the next 30 days
   ([decision #43](../../decisions/README.md#register)).
2. The notification opens a list of those actions, where each one can be
   looked at and undone until it is archived.
3. A month with no such actions sends no notification.

## What the agent sees of health and finance: everything or aggregates only [v1]

Health and money are the most sensitive data; the agent sees single entries
only where the user is talking to it.

**Acceptance criteria**

1. By default the agent sees single entries in chat, and only aggregates
   (sums, averages, counts) in background workflows
   ([decision #42](../../decisions/README.md#register)).
2. Each user can change this separately for health and for finance: let
   background workflows see single entries, or keep chat to aggregates too.
3. A tool that returns health or finance data honours the setting for the
   place it was called from.
