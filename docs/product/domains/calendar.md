# Calendar and planning

Events, time blocks for tasks, and the hours they may be planned into.
This file deepens area 6 of the [feature catalogue](../features.md) into
scenarios and acceptance criteria.
The morning plan and replanning a missed block are described with the
[background workflows](workflows.md).
Only [v1] features are described; the rest stay in the catalogue.

## Events: one-off, repeating, all-day [v1]

**Acceptance criteria**

1. An event has a title, a start and an end, or a date for an all-day
   event, optional notes and an optional place.
2. A repeating event keeps its local time across daylight saving changes.
3. Times are in the time zone from the user's settings.
4. A user sees and changes only their own events; another user's event
   answers `404`.
5. Deleting an event moves it to the shared trash
   ([decision #31](../../decisions/README.md#register)).

## Time blocks for tasks [v1]

A block is time set aside in the calendar for one task.

**Acceptance criteria**

1. A block belongs to one task and has a start and an end.
2. A block is as long as the task's estimate, or 30 minutes without one
   ([decision #51](../../decisions/README.md#register)).
3. Completing or cancelling the task removes its future blocks.
4. A task that does not fit into one free gap is split into several blocks,
   if it can be split ([decision #63](../../decisions/README.md#register)).
5. Every task has a "can be split" flag, on by default; the agent turns it
   off when the task clearly cannot be split, for example a meeting or a
   call, and the user can change it.

## Working hours and days per project, buffer between items [v1]

Blocks are planned only into the hours that fit the project.

**Acceptance criteria**

1. Each user has default working hours and days, for example Monday to
   Friday 9:00–18:00; a project can set its own
   ([decision #61](../../decisions/README.md#register)).
2. A block for a task is planned only inside its project's hours, or the
   user's default hours for a task in the inbox or in a project without
   hours of its own.
3. A buffer, 10 minutes by default, is kept between a block and the item
   before or after it; it is one setting per user
   ([decision #64](../../decisions/README.md#register)).

## Free time lookup [v1]

**Acceptance criteria**

1. "When am I free on Thursday?" lists the gaps between events and blocks
   inside the working hours, after the buffer.
2. The same lookup is what the morning plan uses to place blocks.

## Day, week and month views [v1]

**Acceptance criteria**

1. Events and blocks are shown by day, by week and by month.
2. Views are in the user's time zone and start the week on the day set by
   the UI language, unless the user sets another
   ([decision #76](../../decisions/README.md#register)).
