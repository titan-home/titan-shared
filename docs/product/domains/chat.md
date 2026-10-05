# Chat and agent

How a person talks to the assistant.
This file deepens area 3 of the [feature catalogue](../features.md) into
scenarios and acceptance criteria.
Only [v1] features are described; the rest stay in the catalogue.

## Threads: create, list, rename, delete [v1]

Conversations are kept as threads that the user can come back to, rename and
delete.

**Acceptance criteria**

1. A user sees and changes only their own threads; another user's thread
   answers `404`.
2. The list is ordered by the last message and paged.
3. Deleting a thread moves it to the trash without asking; an Undo is shown
   for a few seconds ([decision #84](../../decisions/README.md#register)).
4. A thread in the trash can be restored for 30 days; after that it is
   deleted for good ([decision #31](../../decisions/README.md#register)).
5. Audit log entries about what the agent did in a thread stay when the
   thread is deleted.

6. The user can empty the trash, or delete one thread from it for good, at
   any time.

## Replies streamed word by word (SSE) [v1]

The reply appears as Claude writes it, not all at once at the end.

**Acceptance criteria**

1. The reply streams over server-sent events.
2. Text reaches the client through nginx as it comes, with no buffering; an
   end-to-end test checks this through the real nginx config.
3. Losing the connection never clears what is on screen.
4. A turn whose client disconnected keeps running on the node to the end,
   and its reply is stored ([decision #36](../../decisions/README.md#register)).
5. A client that comes back while the turn is still running shows that the
   reply is still being written, then shows the whole reply once it is done.

## Tool activity visible, with readable translated tool names [v1]

The user sees what the agent is doing while it works.

**Acceptance criteria**

1. Every tool call shows its translated name, its one-line summary and
   whether it succeeded, for example "Creating a task: buy milk ✓".
2. Each user chooses in their settings between brief and detailed; detailed
   also lets them expand the call's input and result
   ([decision #34](../../decisions/README.md#register)).
3. Brief is the default.

## Approvals inside the reply stream [v1]

An action that needs approval shows up in the reply as a card with Approve
and Reject.
The rules are described with the autonomy area.

## Replies in the language of the message, mixed languages [v1]

The agent answers in the language the user just wrote in, whatever it is.

**Acceptance criteria**

1. The reply is in the language of the last message.
2. A message that mixes languages gets a reply in its main language.
3. This holds for any language, Chinese and Japanese included, not only for
   the UI languages.

## Automatic thread titles [v1]

A new thread gets a short title of its own, so the list stays readable.

**Acceptance criteria**

1. After the first reply, the fast model gives the thread a title in the
   thread's language.
2. The user can rename a thread at any time.
3. A title the user set is never replaced automatically.

## Retry when a Claude reply stalls [v1]

A reply that stops coming does not leave the turn hanging.

**Acceptance criteria**

1. After 60 seconds without anything from Claude, the turn is retried once,
   automatically ([decision #32](../../decisions/README.md#register)).
2. Only time spent waiting for Claude counts; time spent running a tool does
   not.
3. If the retry stalls too, the user sees a short message and a Retry
   button.
4. A retry does not duplicate what a tool already did: tools are idempotent,
   as the development rules require.

## Token usage recorded for every turn [v1]

**Acceptance criteria**

1. Every turn records the model and its input, output, cache-write and
   cache-read tokens.
2. No cost is stored; it is computed from the tokens and a price table when
   shown ([decision #35](../../decisions/README.md#register)).

## Model choice per step: fast and strong [v1]

Each step uses the model that is good enough for it, to save the
subscription's limits.

**Acceptance criteria**

1. Conversation and planning use the strong model.
2. Thread titles and small parsing steps use the fast model
   ([decision #33](../../decisions/README.md#register)).
3. In the working version the user does not choose the model.

## Prompt caching [v1]

Unchanged parts of a turn's prompt are read from the cache instead of being
processed again.

**Acceptance criteria**

1. Caching is on: the Agent SDK caches by default, and nothing on the node
   turns it off.
2. Cache-write and cache-read tokens are recorded with every turn, so a
   second turn in a thread shows cache reads.
