# Notes, knowledge and memory

What the user writes down, what the agent finds in it, and what the agent
remembers about the user.
This file deepens area 9 of the [feature catalogue](../features.md) into
scenarios and acceptance criteria.
Only [v1] features are described; the rest stay in the catalogue.

## Markdown notes with tags [v1]

**Acceptance criteria**

1. A note has a title, a Markdown body and tags.
2. Notes are stored in the language they were written in.
3. A user sees and changes only their own notes; another user's note
   answers `404`.
4. Deleting a note moves it to the shared trash
   ([decision #31](../../decisions/README.md#register)).

## Word search in every script, Chinese and Japanese included [v1]

**Acceptance criteria**

1. One search covers notes, tasks and facts; each result says what it is
   ([decision #73](../../decisions/README.md#register)).
2. Words are found in any script, including Chinese and Japanese text with
   no spaces between words.
3. Search text is never written to any log.

## Search by meaning across languages with a local model [v1]

"What did I note about the car service?" finds the note even if it was
written in another language.

**Acceptance criteria**

1. Notes are turned into vectors by the local embeddings model on the
   node; the text never leaves the node for this
   ([decision #12](../../decisions/README.md#register)).
2. A query in one language finds notes written in another.
3. Indexing happens in the background within a minute of a change.
4. Search by meaning covers notes, tasks and facts, like word search
   ([decision #73](../../decisions/README.md#register)).

## Memory: facts about the user the agent learns from chats and notes [v1]

The agent remembers what it learns about the user, in the open.

**Acceptance criteria**

1. A fact is one sentence in the language it was learned in, with the date
   and a link to its source, a message or a note
   ([decision #71](../../decisions/README.md#register)).
2. The agent sees all of the user's facts on every turn.
3. The agent remembers a fact on its own when it learns something lasting
   about the user, and on request ("remember that …")
   ([decision #72](../../decisions/README.md#register)).
4. Remembering is a `write-internal` action: by default it runs at once and
   the reply shows "remembered: …" with an Undo button.
5. Facts about health and finance come only from what the user says, never
   from tracker entries.

## View, correct and delete facts [v1]

**Acceptance criteria**

1. The user sees every fact with its date and source.
2. A fact can be edited or deleted; a deleted fact goes to the shared
   trash ([decision #31](../../decisions/README.md#register)).
3. The agent may update a fact the user corrected when it learns something
   newer; like any remembering, the change is shown with Undo, so the user
   can object.

## Agent answers that link to the notes and facts they use [v1]

**Acceptance criteria**

1. When a reply draws on a note or a fact, it links to it as an ordinary
   Markdown link with an internal address, for example
   `[the car service note](titan://notes/<id>)`
   ([decision #74](../../decisions/README.md#register)).
2. The web UI opens the item from the link; the CLI shows the link text.
3. The `titan://` scheme is part of the API contract.
