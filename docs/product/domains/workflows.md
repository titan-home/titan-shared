# Background workflows

Work the agent does on its own, on a schedule, without being asked.
This file deepens area 11 of the [feature catalogue](../features.md) into
scenarios and acceptance criteria.
Only [v1] features are described; the rest stay in the catalogue.

## Morning plan [v1]

Every morning the day is planned before it starts: events, and blocks for
the tasks that are due.

**Acceptance criteria**

1. At a time the user sets, by default the start of the working day, the
   agent places blocks for the tasks due today and the overdue ones, in
   priority order ([decision #60](../../decisions/README.md#register)).
2. If the user asked for the plan earlier that day, for example "plan my
   day", the scheduled run does nothing.
3. The blocks are created at once; the plan comes as a notification,
   and every block can be undone like any other agent action.
4. Health and finance data reach the plan only as aggregates, unless the
   user allowed more ([decision #42](../../decisions/README.md#register)).
5. A day with no events and no due tasks sends no plan.

## Replanning a missed block [v1]

A block is missed when its time has passed and its task is still open.

**Acceptance criteria**

1. Whether a missed block is moved depends on the task's due date
   ([decision #62](../../decisions/README.md#register)):

   | Task | Meaning | What happens |
   |---|---|---|
   | Due date with a time, and it has passed | Already lost | The block is not moved; the task is marked overdue and goes into tomorrow's morning plan, where the agent asks what to do with it |
   | Due date without a time, or none | Can still be done | The block moves to the nearest free time today, or to tomorrow; the user is told, and it can be undone |

2. A block is moved at most once a day.
3. The check runs 15 minutes after the block ends.
