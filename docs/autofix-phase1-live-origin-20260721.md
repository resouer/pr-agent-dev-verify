# Auto-fix Phase 1 — Live Origin QA (2026-07-21)

QA note for Phase 1 Auto-fix live verification after the PR-origin deployment.

This disposable PR verifies the provider-backed origin lifecycle: a
`pull_request`-triggered workflow runs a single Ubuntu shell job whose test
step fails deterministically (exit 1) so that Auto-fix can observe and act on a
failing check originating from the PR itself.

- Scope: live verification only.
- Expected state: the "Auto-fix Phase 1 Origin QA" check fails on purpose.
- Do not merge; this branch and PR are disposable.
