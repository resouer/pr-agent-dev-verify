# Auto-fix No-Goal Live Verify

Disposable QA fixture to verify the platform Auto-fix path without a session
`/goal`.

A `pull_request` workflow runs the **Auto-fix Hibernated E2E QA** check, which
greps `.autofix-ordering-state` and requires it to equal `green`. The state file
is seeded as `red` so the check fails, leaving the PR red for the platform
Auto-fix to pick up.
