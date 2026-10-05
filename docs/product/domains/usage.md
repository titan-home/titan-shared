# Claude usage

How much of the Claude subscription TITAN spends.
This file deepens area 12 of the [feature catalogue](../features.md) into
scenarios and acceptance criteria.
Only [v1] features are described; the rest stay in the catalogue.

## A usage screen: tokens and estimated cost per month, by model [v1]

The user sees what their assistant costs, in the CLI and on the web.

**Acceptance criteria**

1. For the current month and every past one: input, output, cache-write
   and cache-read tokens, by model, and the cost computed from them with a
   price table ([decision #35](../../decisions/README.md#register)).
2. The cost is marked as an estimate: the subscription is not billed per
   token.
3. Each user sees only their own usage; a report across members comes with
   the household.
