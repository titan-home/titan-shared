# Clients

Where the user meets TITAN: the CLI first, then the browser, then a minimal
Android app for notifications.
This file deepens area 14 of the [feature catalogue](../features.md) into
scenarios and acceptance criteria.
Only [v1] features are described; the rest stay in the catalogue.

## CLI: sign-in, chat, every domain, administration [v1]

**Acceptance criteria**

1. `titan login`, `titan logout` and `titan whoami` work as described with
   [accounts](accounts.md).
2. `titan chat` streams a reply and shows tool activity and approvals;
   `titan approve` decides a pending request.
3. Every domain can be read and changed from the CLI.
4. Administration covers the items in the table below.

## Web: sign-in, chat, node management, every domain [v1]

**Acceptance criteria**

1. Password sign-in with a session cookie, chat with approvals, and every
   domain, as described with their areas.
2. Node management: service health, updates and rollback, backups and
   restore, the certificate.

## Android app, minimal: sign-in and notifications [v1]

The phone rings at the right moment, without any external app
([decisions #14, #23](../../decisions/README.md#register)).

**Acceptance criteria**

1. Sign-in with username and password pairs the phone as a device.
2. The app keeps its own connection to the node, the notification stream
   over the API, in a background service; it asks once for an exemption
   from battery optimisation and explains why.
3. Every notification is shown as an Android notification with its
   actions: Snooze and Done for reminders, Approve and Reject for
   approvals.
4. On reconnect the app fetches everything since the last notification it
   saw and shows each one once ([decision #58](../../decisions/README.md#register)).
5. Losing the connection never clears what is on screen.

## Light and dark themes [v1]

**Acceptance criteria**

1. Every screen has a light and a dark theme, following the system setting
   by default; the user can pin one.
2. Both themes meet the contrast rule from the development rules.

## What administration includes in the working version

| Where | What |
|---|---|
| A command on the node's machine only | Create the owner; reset the owner's password ([decision #30](../../decisions/README.md#register)) |
| CLI and web | Devices and revoking them; settings: time zone, region, UI language, working hours, buffer, autonomy modes, health and finance visibility, token lifetime; Claude usage |
| CLI and web, from build-plan stages 4 and 5 | Service health, updating the node to a release manifest and rolling back, backups and restore, the certificate |
