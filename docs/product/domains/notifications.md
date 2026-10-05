# Notifications and delivery

How reminders, approvals and other news reach the user: in a history, in
the web UI's bell, and on the phone through the Android app.
This file deepens area 8 of the [feature catalogue](../features.md) into
scenarios and acceptance criteria.
Only [v1] features are described; the rest stay in the catalogue.

## Notification history, read and unread [v1]

**Acceptance criteria**

1. Every notification is kept in the user's history, read or unread.
2. Opening a notification, or acting on it (Snooze, Done, Approve, Reject),
   marks it read on every device.
3. Notifications older than one year are deleted
   ([decision #57](../../decisions/README.md#register)).
4. A user sees only their own notifications; another user's notification
   answers `404`.

## Notifications delivered to the Android app over its own connection [v1]

At the right moment the phone shows the notification with its actions
([decision #14](../../decisions/README.md#register)).

**Acceptance criteria**

1. The API serves a notification stream per device over server-sent
   events, authenticated by the device token like any call; it carries only
   that user's notifications ([decision #56](../../decisions/README.md#register)).
2. A new notification reaches a connected app within seconds of being
   created.
3. The stream goes through nginx on 443 like everything else; the node
   exposes nothing else ([decision #59](../../decisions/README.md#register)).

## The app catches up on reconnect; nothing is lost or shown twice [v1]

**Acceptance criteria**

1. When the app reconnects, it asks for every notification since the last
   one it saw; the node never retries on its own
   ([decision #58](../../decisions/README.md#register)).
2. Each notification is shown once, by its id, however many times it
   arrives.
3. A notification the app never received still stays in the history and
   the bell.

## A bell in the web UI, checked about once a minute [v1]

**Acceptance criteria**

1. The bell shows the number of unread notifications and opens the
   history.
2. The web UI checks for new notifications about once a minute.
