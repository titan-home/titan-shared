# Accounts and access

How people and their devices get into TITAN.
This file deepens area 2 of the [feature catalogue](../features.md) into
scenarios and acceptance criteria.
Only [v1] features are described; the rest stay in the catalogue.

## Create the owner at install time [v1]

Whoever installs the node creates the owner account with one command on the
node, before any client can sign in.

**Acceptance criteria**

1. The command asks for a username and a password and creates the owner.
2. The password is stored only as an Argon2id hash.
3. The password is never printed, logged or passed on the command line.
4. The password has at least 8 characters.
5. Until the owner exists, every sign-in attempt fails.
6. If an owner already exists, the command refuses and changes nothing.
   Resetting a forgotten password is a
   [separate feature](#reset-the-owners-forgotten-password-v1).

## Sign in with username and password [v1]

The owner signs in from the CLI or the browser with a username and password
and gets a device token or a browser session.

**Acceptance criteria**

1. Right username and password: the CLI gets a
   [device token](#device-tokens-pairing-the-cli-a-browser-and-the-android-app-v1); the
   browser gets a [session cookie](#browser-sessions-in-an-httponly-cookie-v1).
2. Wrong username or wrong password: the same error, so it does not reveal
   whether the username exists.
3. Failed attempts count towards the
   [guessing limit](#password-guessing-limited-per-client-address-and-account-v1).
4. The password never appears in logs.
5. `titan whoami` shows who is signed in on this device.

## Device tokens: pairing the CLI, a browser and the Android app [v1]

Every device gets its own token, so one lost device can be cut off without
touching the others.

**Acceptance criteria**

1. The first sign-in from a CLI creates a new device with its own token.
2. Signing in again from a CLI that still holds its token replaces that
   token: the old one stops working, and the device keeps its entry
   ([decision #24](../../decisions/README.md#register)).
3. A token is `titan_v1_` followed by 32 random bytes in base64url
   ([decision #29](../../decisions/README.md#register)).
4. The node stores only the token's SHA-256 hash; the token itself is shown
   to the device once.
5. A request with an unknown or revoked token gets `401`.
6. The token never appears in logs.
7. The Android app signs in and is paired like any other device
   ([decision #23](../../decisions/README.md#register)).
8. A token not used for 90 days expires. Each user can set a shorter or a
   longer limit, or none, in their settings; the same setting applies to
   their browser sessions ([decision #25](../../decisions/README.md#register)).

## List devices and revoke a device [v1]

The owner sees every device that can reach their account and cuts off any of
them.

**Acceptance criteria**

1. The list shows every device and browser session: name, when it was paired,
   when it was last used.
2. Revoking a device stops its very next request with `401`.
3. Revoking is recorded in the audit log.
4. A user sees and revokes only their own devices; another user's device
   answers `404`.
5. The device you are using can revoke itself; it is signed out at once.

## Browser sessions in an HttpOnly cookie [v1]

In the browser the session lives in a cookie that no script can read.

**Acceptance criteria**

1. The cookie is `HttpOnly`, `Secure` and uses the `__Host-` prefix.
2. No token is ever readable from JavaScript or stored in browser storage.
3. A session not used for 90 days expires; every use extends it. The limit
   is the same user setting as for device tokens ([decision #25](../../decisions/README.md#register)).
4. The cookie is `SameSite=Lax`.
5. Any request other than `GET` or `HEAD` whose `Origin` is not the node's
   own address is refused with `403` ([decision #26](../../decisions/README.md#register)).
6. `GET` and `HEAD` requests never change anything.

## Sign out [v1]

Signing out ends the device's access on the node, not only on the device.

**Acceptance criteria**

1. In the browser, signing out ends the session on the node and clears the
   cookie.
2. In the CLI, `titan logout` revokes the device's token on the node and
   deletes the local copy.
3. The device disappears from the device list.

## Password guessing limited per client address and account [v1]

Guessing a password is slowed down without letting anyone lock the owner
out.

**Acceptance criteria**

1. After 10 failures within 15 minutes from one client address for one
   account, only that pair is refused for 15 minutes; the account stays open
   from other addresses ([decision #27](../../decisions/README.md#register)).
2. `X-Forwarded-For` is trusted only from a configured list of our own
   proxies; otherwise the connection's address counts.
3. A refused attempt gets `429` with `Retry-After`, the same answer whether
   or not the password was right.

## Change password [v1]

The owner changes their password from any signed-in client.

**Acceptance criteria**

1. The current password is required.
2. The new password follows the same rules as at creation.
3. The change is recorded in the audit log, without either password.
4. Every other device and session of the user is revoked; the one used for
   the change stays signed in ([decision #28](../../decisions/README.md#register)).

## Reset the owner's forgotten password [v1]

An owner who forgot the password gets back in without restoring a backup or
editing the database.

**Acceptance criteria**

1. A command on the node, the same tool that creates the owner, sets a new
   password ([decision #30](../../decisions/README.md#register)).
2. There is no way to reset the password over the API.
3. The new password is asked for, never passed on the command line, and
   follows the same rules as at creation.
4. Every device and session of the owner is revoked.
5. The reset is recorded in the audit log, without the password.
