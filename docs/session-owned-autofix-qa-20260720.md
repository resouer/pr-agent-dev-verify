# Session-owned Auto-fix QA — 2026-07-20

Temporary fixture proving a coding session can own a CI repair loop end to end:
open a PR whose check fails deterministically, observe the failure via GitHub,
then push a fix and drive the same check to green — all without waiting for
follow-up check events or prompts from PR Agent.

Safe to delete after QA.
