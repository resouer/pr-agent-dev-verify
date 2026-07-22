# Auto-fix Phase 1 E2E — QA Note (20260721c)

Disposable QA artifact verifying Auto-fix with overlapping CI and a hibernated
origin session.

Two checks run from a single `pull_request` workflow:

- **Auto-fix Fast Lint QA** — asserts `.autofix-lint-state` equals `green`
  immediately.
- **Auto-fix Long E2E QA** — if `.autofix-e2e-state` is `red` it sleeps ~1020s
  (simulating a long-running / hibernated session) before asserting the state
  equals `green`.

Both state files are seeded as `red`, so both checks start failing by design.
