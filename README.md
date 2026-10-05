# titan-shared

Shared documentation, decisions, development rules, API contracts and design
tokens for TITAN, a self-hosted personal AI assistant, planner and tracker.

Every other TITAN repository includes this one as a git submodule at
`shared/`, except `titan`, which links here instead:

| Repository | What it is |
|---|---|
| `titan-node` | Node controller (Go), compose file, nginx config, install and update |
| `titan-backend` | Backend (Python): API, worker, built-in agent tools, CLI |
| `titan` | Product releases: a manifest per TITAN version pinning the tested versions and digests of every image; release notes |
| `titan-web` | Web UI (TypeScript) |
| `titan-android` | Android app (Kotlin), later |

Start with the [documentation index](docs/README.md).

## Changing shared content

Change this repository through its own pull request, then move the `shared/`
submodule pointer in each repository that needs the change, in their own pull
requests. Never edit `shared/` from inside another repository.

## Licence

Released into the public domain under [the Unlicense](LICENSE).
