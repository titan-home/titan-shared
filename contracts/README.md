# API contracts

The OpenAPI contract of the TITAN API lives here and is the source of truth
for every client. It arrives with build-plan stage 1.

- `openapi.json` — the contract of `/api/v1`. FastAPI generates it from the
  backend's code; it is copied here, never written by hand
  ([decision #87](../docs/decisions/README.md#register)).
- The backend (`titan-backend`) checks in CI that it serves exactly this contract.
- Nothing enters the contract by accident: every route declares its response
  model, errors are one `application/problem+json` schema instead of
  FastAPI's default validation error, and internal routes are left out of
  the schema.
- A pull request that changes the contract lists every added or changed
  operation and field with the acceptance criterion it serves. Whatever
  serves no criterion is removed.
- Clients (`titan-web`, `titan-android`, the CLI) generate their API code from
  it through their `shared/` submodule; generated code is never edited by
  hand.
- A contract change is its own pull request here, followed by pull requests
  that move the `shared/` pointer in the backend and the clients.
- Rules for the API itself are in [development rules, section 9](../docs/development/rules.md#9-api-and-contracts).
