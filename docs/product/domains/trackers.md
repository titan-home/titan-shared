# Trackers

Numbers about the user's life, logged by a phrase and summed up by period:
habits, weight, sleep, workouts, mood, money.
This file deepens area 10 of the [feature catalogue](../features.md) into
scenarios and acceptance criteria.
Only [v1] features are described; the rest stay in the catalogue.

## Templates: habit, weight, sleep, workout, mood, expense, income [v1]

A template is a preset: a tracker is created from it and then edited like
any other.

**Acceptance criteria**

1. Creating a tracker from a template sets its name, unit, bounds and kind
   of target ([decision #66](../../decisions/README.md#register)).
2. Everything a template set can be changed afterwards; the defaults are:

   | Template | Unit | Target kind |
   |---|---|---|
   | habit | times | at least, with a schedule |
   | weight | kg | — |
   | sleep | hours | at least |
   | workout | minutes | at least |
   | mood | scale 1–5 | — |
   | expense | the user's currency | at most |
   | income | the user's currency | — |

## Custom trackers with a unit and bounds [v1]

**Acceptance criteria**

1. A tracker has a name, a unit and optional lower and upper bounds for a
   value; a value outside the bounds is refused.
2. An entry holds one value in the tracker's unit, a moment in time, an
   optional interval (from, to) and an optional note; a habit entry is
   the value 1 ([decision #65](../../decisions/README.md#register)).
3. An expense or income entry also has a category.
4. A user sees and changes only their own trackers and entries; another
   user's answer `404`.
5. Deleting a tracker moves it with its entries to the shared trash
   ([decision #31](../../decisions/README.md#register)).

## Targets per day, week or month, "at least" or "at most" [v1]

**Acceptance criteria**

1. A target is a value per day, week or month, either "at least" or "at
   most" ([decision #67](../../decisions/README.md#register)).
2. An "at least" period counts as met as soon as the sum reaches the
   target; an "at most" period counts as met when it ends with the sum
   under the limit.
3. Periods are counted in the user's time zone.

## Logging by a phrase in chat, in any language [v1]

"Spent 23.40 on groceries", "slept 7 hours", "ran 5 km": one phrase, one
entry.

**Acceptance criteria**

1. The agent picks the tracker, the value, the unit, the time and, for
   money, the category from the phrase, in any language.
2. Numbers and amounts are parsed in any language's notation, for example
   "23,40" and "23.40".
3. Logging is a `write-internal` action and so, by default, runs at once
   and shows an Undo button ([decision #38](../../decisions/README.md#register)).
4. Money is in the user's currency, from their settings. An amount in
   another currency ("spent 20 euros") is stored as given, with its
   currency, and marked as foreign; it is not converted and not added to
   the sums ([decision #68](../../decisions/README.md#register)).

## Streaks and statistics per period [v1]

**Acceptance criteria**

1. A streak is the number of met periods in a row up to now.
2. For a habit with a schedule, only the days it is due count.
3. Statistics per day, week and month: sum, average, minimum, maximum and
   number of entries.

## Charts [v1]

**Acceptance criteria**

1. A line chart for measurements (weight, sleep, mood), a bar chart per
   period for sums (expenses, workouts, habits), and a pie chart of
   expenses by category ([decision #70](../../decisions/README.md#register)).
2. Each chart shows a week, a month or a year; the target, where there is
   one, is drawn over it.

## Expense and income categories [v1]

**Acceptance criteria**

1. Each money tracker has its own list of categories, which the user edits
   ([decision #69](../../decisions/README.md#register)).
2. The expense and income templates come with a starter list, for example
   groceries, transport, housing, health, eating out, leisure, clothes,
   other; and salary, other.
3. Every list has an "other" category that cannot be deleted.
4. When logging by a phrase, the agent picks the category by meaning;
   when none fits, it uses "other".

## Habit schedule (the days it is due) [v1]

**Acceptance criteria**

1. A habit says on which days of the week it is due, every day by default.
2. A day it is not due does not break the streak.
