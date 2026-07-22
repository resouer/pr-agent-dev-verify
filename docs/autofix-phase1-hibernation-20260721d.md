# Auto-fix Phase 1 Hibernation — QA Note (20260721d)

Disposable QA fixture verifying Phase 1 Auto-fix waking a hibernated origin
session.

The `pull_request` workflow runs a single **Auto-fix Hibernated E2E QA** job:

- On the initial `red` head, the job sleeps ~1020s (past the 15-minute idle
  hibernation window) and then asserts `.autofix-hibernation-state` equals
  `green`, so it fails.
- On a fixed `green` head, the sleep branch is skipped and the assertion passes
  immediately.

The state file is seeded as `red`, so the check starts failing by design.
