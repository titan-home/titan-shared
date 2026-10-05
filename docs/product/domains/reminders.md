# Reminders

Telling the user about something at the right moment, exactly once.
This file deepens area 7 of the [feature catalogue](../features.md) into
scenarios and acceptance criteria.
Only [v1] features are described; the rest stay in the catalogue.

## One-off and repeating [v1]

"Remind me tomorrow at 9 to buy milk": the user asks in any language, and
at 9:00 the reminder arrives.

**Acceptance criteria**

1. A reminder is either on its own or attached to a task or an event.
2. A repeating reminder moves to its next time when it fires and keeps its
   local time across daylight saving changes.
3. Times are in the time zone from the user's settings.
4. A reminder of a task that is done, cancelled or in the trash does not
   fire.
5. A user sees and changes only their own reminders; another user's
   reminder answers `404`.

## Fire within 60 seconds, never twice [v1]

**Acceptance criteria**

1. A reminder fires no later than 60 seconds after its time.
2. Firing creates exactly one notification: its id is derived from the
   reminder and the time, so a second firing cannot create a duplicate.
3. A reminder whose time passed while the node was down fires once after
   the node starts, marked with how late it is, for example "2 h late"
   ([decision #55](../../decisions/README.md#register)).
4. Of a repeating reminder, only the last missed time fires.

## Snooze and Done [v1]

The user deals with a reminder in one tap.

**Acceptance criteria**

1. Snooze offers 10 minutes, 1 hour, and tomorrow at the start of the
   working day; any other time is asked for in chat, for example "snooze
   until the evening" ([decision #53](../../decisions/README.md#register)).
2. Done on a reminder of a task completes the task, and it can be undone
   ([decision #54](../../decisions/README.md#register)).
3. Done on a reminder of its own closes the reminder.
4. A reminder is dealt with once; a second Snooze or Done, from any device,
   changes nothing.

## Default reminders for tasks with a due time and for events [v1]

Nobody has to ask for a reminder about a meeting or a task with a time.

**Acceptance criteria**

1. A task with a due time is reminded at that time; an event 15 minutes
   before it starts ([decision #52](../../decisions/README.md#register)).
2. Each user can change both defaults in their settings.
3. A single task or event can have a different reminder, or none.
4. A task with a due date but no time gets no default reminder.
