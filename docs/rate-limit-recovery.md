# Rate-limit recovery

When a client exceeds its allowed request rate the service responds with
`429 Too Many Requests`. This document describes how a well-behaved client
recovers.

## Recognizing a rate-limit response

A `429` is accompanied by headers that describe the limit and when to retry:

| Header | Meaning |
|--------|---------|
| `Retry-After` | Seconds to wait before the next request is allowed. This is authoritative. |
| `X-RateLimit-Limit` | Requests permitted per window. |
| `X-RateLimit-Remaining` | Requests left in the current window. |
| `X-RateLimit-Reset` | Epoch second at which the window resets. |

## Recovery rules

1. **Honor `Retry-After` first.** When present, wait at least that long before
   retrying. It reflects the server's actual state and overrides any local
   backoff estimate.
2. **Back off exponentially with jitter** when `Retry-After` is absent. Start
   from a base delay and double it on each successive `429`, adding random
   jitter so that many clients recovering at once do not resynchronize into a
   new spike (the thundering-herd problem).
3. **Cap the delay and the attempts.** Bound the backoff at a maximum delay and
   a maximum retry count; surface a failure to the caller rather than retrying
   forever.
4. **Retry only the throttled request.** A `429` means "not now," not "this
   failed." The request was not processed, so retrying is safe and does not
   require idempotency guarantees — but do not escalate to a different endpoint
   or duplicate the work.

## Avoiding rate limits proactively

- Watch `X-RateLimit-Remaining`. When it approaches zero, slow the send rate
  before hitting the limit rather than driving into a wall of `429`s.
- Spread bursts of work over time instead of issuing them all at once.
- Prefer a single shared client with a coordinated limiter over many
  independent clients that each believe they have the full budget.

## What not to do

- Do **not** retry immediately in a tight loop; that extends the throttle.
- Do **not** ignore `Retry-After` in favor of a shorter local delay.
- Do **not** treat a `429` as a server error (`5xx`); it is a signal to slow
  down, not evidence of an outage.
