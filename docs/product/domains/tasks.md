# Tasks and projects

What the user has to do, grouped into projects.
This file deepens area 5 of the [feature catalogue](../features.md) into
scenarios and acceptance criteria.
Only [v1] features are described; the rest stay in the catalogue.

## Tasks: title, notes, due date, priority, tags, status [v1]

The user, or the agent on the user's behalf, keeps a list of things to do.

**Acceptance criteria**

1. A task has a title, Markdown notes, a due date, a priority from 1 to 4,
   tags and a status.
2. The status is `open`, `done` or `cancelled`
   ([decision #44](../../decisions/README.md#register)).
3. The due date may carry a time or not, for example "on Friday" or "on
   Friday at 15:00" ([decision #45](../../decisions/README.md#register)).
4. Dates and times are in the time zone from the user's settings.
5. A user sees and changes only their own tasks; another user's task
   answers `404`.
6. Deleting a task moves it to the trash, the same trash as for chat
   threads, restorable for 30 days
   ([decision #31](../../decisions/README.md#register)).
7. Priority 1 is the highest. Clients show words, not numbers: 1 urgent,
   2 high, 3 normal, 4 low ([decision #47](../../decisions/README.md#register)).
8. A new task is normal (3), unless a priority is given.
9. Checklists live in the task's notes as Markdown (`- [ ]`); subtasks come
   later.
10. A task has a "can be split" flag for planning, described with the
    [calendar](calendar.md#time-blocks-for-tasks-v1).

## Repeating tasks [v1]

A task that comes back, either on a schedule or some time after it was
done.

**Acceptance criteria**

1. Each repeating task follows one of two rules
   ([decision #46](../../decisions/README.md#register)):

   | Rule | Example | Next time |
   |---|---|---|
   | On a schedule | "every Monday" | The next Monday, whenever it was done |
   | After completion | "7 days after it is done" | 7 days after the day it was done |

2. Completing a repeating task creates its next occurrence at once.
3. A repeating task keeps its local time across daylight saving changes.
4. There are two separate actions: "skip this time" creates the next
   occurrence, "stop repeating" ends the series
   ([decision #48](../../decisions/README.md#register)).

## Projects, inbox, archive [v1]

Tasks are grouped into projects; a task without a project is in the inbox.

**Acceptance criteria**

1. A task belongs to one project or to none; a task with no project is in
   the inbox.
2. Deleting a project moves it to the trash together with its tasks;
   restoring it brings the tasks back too.
3. An archived project and its tasks are hidden from lists and from the
   daily plan; search still finds them, marked as archived
   ([decision #49](../../decisions/README.md#register)).
4. An archived project can be brought back with its tasks as they were.

## Filters, saved filters, search, sorting [v1]

The user finds the tasks that matter now without scrolling through all of
them.

**Acceptance criteria**

1. Built-in filters ([decision #50](../../decisions/README.md#register)):
   - today: due today, and overdue;
   - the next 7 days;
   - the inbox;
   - by project, by tag, by priority.
2. The user can save their own filter, for example "urgent at work", and
   use it like a built-in one.
3. Search finds words in titles and notes in any language, Chinese and
   Japanese included.
4. Tasks can be sorted by due date (the default), by priority or by when
   they were created.

## Estimates and links to plan time blocks [v1]

A task can say how long it takes, so the daily plan gives it a block of the
right size.

**Acceptance criteria**

1. An estimate is optional and given in minutes; the agent understands
   phrases such as "about two hours" ([decision #51](../../decisions/README.md#register)).
2. The daily plan gives a task a block as long as its estimate, or 30
   minutes without one.
3. The agent can estimate a task itself, for example while planning the
   day; that is an ordinary change to the task, visible and undoable like
   any other.
4. How a task and its blocks in the calendar are linked is described with
   the calendar area.
