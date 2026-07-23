# Auto-fix Fresh NoGoal QA

This document is part of a live verification exercise for the platform Auto-fix
capability in a no-goal scenario.

The companion state file `.autofix-fresh-state` drives the
"Auto-fix Fresh NoGoal QA" GitHub Actions workflow:

- When the state file contains `red`, the workflow check fails.
- When the state file contains `green`, the workflow check passes.

The workflow is expected to start red so that the platform Auto-fix can perform
the repair by flipping the state to `green`.
