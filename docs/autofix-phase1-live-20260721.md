# Auto-fix Phase 1 Live QA — 2026-07-21

Temporary fixture for the Phase 1 Auto-fix live lifecycle verification.

Ships a `pull_request` workflow whose single check **Auto-fix Phase 1 Live QA**
fails deterministically (`exit 1`), so the live Auto-fix lifecycle can be
observed on a real PR. Safe to delete after QA.
