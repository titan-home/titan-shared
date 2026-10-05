# API contracts

The OpenAPI contract of the TITAN API lives here and is the source of truth
for every client. It arrives with build-plan stage 1.

- `openapi.json` — the contract of `/api/v1`.
- The backend (`titan-backend`) checks in CI that it serves exactly this contract.
- Clients (`titan-web`, `titan-android`, the CLI) generate their API code from
  it through their `shared/` submodule; generated code is never edited by
  hand.
- A contract change is its own pull request here, followed by pull requests
  that move the `shared/` pointer in the backend and the clients.
- Rules for the API itself are in [development rules, section 9](../docs/development/rules.md#9-api-and-contracts).
