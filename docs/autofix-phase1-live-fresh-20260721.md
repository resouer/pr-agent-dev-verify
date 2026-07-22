# Auto-fix Phase 1 — Fresh-Session Live Verification (2026-07-21)

## QA Note

This is a **disposable** QA artifact for validating the Phase 1 Auto-fix
live-verification lifecycle in a fresh session.

- The accompanying workflow `.github/workflows/autofix-phase1-live-fresh-20260721.yml`
  runs a single Ubuntu shell job with the visible check name
  **"Auto-fix Phase 1 Fresh QA"**.
- The job's only test step is designed to **fail deterministically** (exit 1)
  so the auto-fix path has a real, reproducible failure to act on.
- No fix is applied in this turn. This PR exists solely to exercise the
  open → failing-check lifecycle.

Safe to close/discard once verification is complete.
