# Languages and time

Nothing in TITAN assumes one language, one script or one time zone.
This file deepens area 15 of the [feature catalogue](../features.md) into
scenarios and acceptance criteria.
Only [v1] features are described; the rest stay in the catalogue.

## UI in English, Russian and Ukrainian [v1]

**Acceptance criteria**

1. Every user-visible string in every client is translated; the three
   languages have the same set of strings, checked in CI.
2. Each user picks the UI language in their settings; a new user gets the
   language of the sign-in page's browser, English in the CLI.

## Any language in data and in chat [v1]

Covered by the other areas; this list points to the criteria:

- replies in the language of the message, mixed languages included
  ([chat](chat.md#replies-in-the-language-of-the-message-mixed-languages-v1));
- word search in every script, Chinese and Japanese included
  ([notes](notes.md#word-search-in-every-script-chinese-and-japanese-included-v1));
- logging by a phrase and number notation in any language
  ([trackers](trackers.md#logging-by-a-phrase-in-chat-in-any-language-v1));
- stored text stays in the language it was written in
  ([notes](notes.md#markdown-notes-with-tags-v1)).

## Time zone from the user's settings [v1]

**Acceptance criteria**

1. Every date and time is computed and shown in the time zone from the
   user's settings, never the server's or the browser's.
2. Repeating items keep their local time across daylight saving changes.
3. Clients send local dates and times with the time zone name.

## Date and number formats from a region setting [v1]

**Acceptance criteria**

1. Each user has a region setting, separate from the UI language, that sets
   the date, time and number formats, for example `05.10.2026` and `23,40`
   ([decision #75](../../decisions/README.md#register)).
2. A new user's region follows their UI language until they change it.
3. The week starts on the day the UI language implies, Monday for Russian
   and Ukrainian, Sunday for English; the user can override it
   ([decision #76](../../decisions/README.md#register)).
