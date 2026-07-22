# Auto-fix Phase 1 Ordering — QA Note (20260722e)

Disposable QA fixture verifying the deployed Phase 1 Auto-fix ordering contract
in Dev.

The `pull_request` workflow runs a single **Auto-fix Hibernated E2E QA** job:

- On the initial `red` head: the delayed-observation branch is skipped and the
  assertion fails immediately (state must be `green`).
- On a fixed `green` head: the job sleeps ~600s to provide a safe in-progress
  observation window before asserting the state equals `green`, then passes.

The marker file is seeded as `red`, so the check starts failing by design.
