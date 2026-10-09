# Node and platform

Installing, running, updating and protecting a node.
This file deepens area 1 of the [feature catalogue](../features.md) into
scenarios and acceptance criteria.
Only [v1] features are described; the rest stay in the catalogue.

## Install a node on a clean machine with one command [v1]

**Acceptance criteria**

1. One command on a clean machine with Docker installs a node from a
   release manifest and starts it.
2. The install ends with the owner created
   ([accounts](accounts.md#create-the-owner-at-install-time-v1)) and the
   web UI reachable over HTTPS.
3. The node test installs on a clean GitHub-hosted runner with a
   self-signed certificate ([decision #82](../../decisions/README.md#register)).

## Run every service with docker compose [v1]

**Acceptance criteria**

1. Every service is a container in one compose file
   ([decision #1](../../decisions/README.md#register)).
2. Containers run as non-root users with read-only file systems where
   possible; only nginx is reachable from outside the node.
3. Every container has a memory limit; the node runs on the reference
   machine with 2 CPU cores and 8 GB of memory.

## Node controller: service health, shown to the owner [v1]

**Acceptance criteria**

1. The controller reports every service's health, as Docker's healthchecks
   see it, and the CLI and the web UI show it
   ([decisions #4, #155](../../decisions/README.md#register)).
2. The controller's Docker access is the most sensitive privilege on the
   node and is guarded accordingly.
3. The controller does not listen on the network. The API calls it over a
   Unix socket inside the node, only for the owner, after its own access
   check ([decision #78](../../decisions/README.md#register)).
4. The controller accepts calls from that socket only.

## Update images to pinned versions and roll back a failed update [v1]

**Acceptance criteria**

1. An update moves the node to a release manifest from the `titan`
   repository; every image is pinned by digest.
2. Before an update that migrates the database, the controller takes a
   backup.
3. A failed update is rolled back to the previous manifest; if the
   database was migrated, the backup is restored.

## Scheduled database backups and restore from a backup [v1]

**Acceptance criteria**

1. Backups run on a schedule and are throttled so the node stays
   responsive.
2. A backup can be restored on the node or on a clean machine; the node
   test does both.
3. Backups are compressed database dumps in a directory on the node's
   disk, not encrypted; the controller keeps the last 7 daily and 4 weekly
   ones and deletes the rest ([decision #79](../../decisions/README.md#register)).
4. Copying backups off the node is the owner's job, with any tool such as
   rsync or Syncthing; the documentation says plainly that a backup on
   the same disk protects against a mistake or a failed update, not
   against losing the machine.

## Node configuration and secrets storage [v1]

**Acceptance criteria**

1. Secrets never enter git, logs or error messages; they live in the
   node's secret store, managed by the controller.
2. The store is a directory on the node with files of mode `0600`; the
   controller creates and rotates them ([decision #77](../../decisions/README.md#register)).
3. Containers get a secret as a read-only mounted file and read its path
   from a `*_FILE` variable; no secret is passed as an environment value.

## nginx as the single entry point, TLS [v1]

**Acceptance criteria**

1. nginx terminates TLS and is the only container reachable from outside
   ([decision #17](../../decisions/README.md#register)).
2. `/` serves the UI files and `/api` proxies to the API without buffering
   SSE; the node exposes nothing else
   ([decision #59](../../decisions/README.md#register)).
3. The stock nginx image is used; the config and the UI files are mounted
   from the node ([decision #19](../../decisions/README.md#register)).
4. The security headers and TLS settings are never weakened without a
   decision in the register.

## Issue and renew the certificate [v1]

**Acceptance criteria**

1. The controller requests the certificate with `tailscale cert` for the
   node's tailnet name and renews it before it expires
   ([decision #18](../../decisions/README.md#register)).
2. The certificate source is one replaceable step, so other sources can
   be added later.

## Images published by CI; nodes pull them ready-made [v1]

**Acceptance criteria**

1. Every image is built and published by CI on a version tag to
   `ghcr.io/titan-home/`, never from a laptop.
2. A release manifest lists each component's version, source commit and
   image digest; CI checks that each image exists and was built from the
   listed commit.
