# Retry behavior

Operations that call external services in `calc-demo` retry transient failures
before giving up.

## Policy

- **Max attempts:** 3 (one initial call plus two retries).
- **Backoff:** exponential, starting at 100 ms and doubling each attempt
  (100 ms, 200 ms), capped at 2 s.
- **Jitter:** a random factor of up to ±20% is applied to each delay to avoid
  thundering-herd retries.

## What is retried

Only transient errors are retried: network timeouts, connection resets, and
`5xx` responses. Deterministic failures — invalid arguments, `4xx` responses,
and assertion errors — fail immediately without retrying.

## Idempotency

Retries assume the operation is safe to repeat. Non-idempotent operations must
opt out of retries explicitly; otherwise a partially applied side effect could
be duplicated.

## Observability

Each retry is logged with the attempt number and the delay before the next try,
so repeated retries are visible when diagnosing latency.
