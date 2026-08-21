# Release rollback

When a release of `calc-demo` misbehaves, roll back to the last known-good
version rather than trying to hot-fix forward under pressure.

## When to roll back

Roll back if a newly released version causes any of the following that was not
present in the prior version:

- A spike in error rate or latency (see [observability](observability.md)).
- A regression in a published function's results.
- A failed post-deploy smoke check.

## Procedure

1. **Identify** the last known-good version from the release log.
2. **Pin** deployments to that version (re-publish the previous tag or revert
   the version bump).
3. **Verify** by re-running the smoke checks against the pinned version.
4. **Announce** the rollback in the release channel with the reason and the
   version rolled back to.

## After rolling back

- Open an issue capturing the failure and the offending version.
- Keep the bad version yanked until a fix lands and passes CI.
- Add a regression test that reproduces the failure before re-releasing.

## Compatibility

Rollback is only safe when the release made no backward-incompatible data or
API changes. Migrations that cannot be reversed must ship behind a flag so the
code can be rolled back independently of the data.
