# Auto-fix Phase 1 E2E — QA Note (20260721b)

This is a disposable QA artifact for final Phase 1 Auto-fix Dev acceptance.

The accompanying workflow runs a single Ubuntu shell job that asserts the
contents of `.autofix-qa-state` equal `green`. The state file is seeded as
`red` so the check starts failing, exercising the Auto-fix Dev lifecycle.
