# Health-check behavior and failure interpretation

The service exposes a health endpoint used by orchestrators and load balancers
to decide whether an instance should receive traffic.

## Endpoint

`GET /healthz` returns a status code and a small JSON body:

```json
{ "status": "ok", "checks": { "db": "ok", "cache": "ok" } }
```

## Status semantics

| HTTP status | `status` field | Meaning |
|-------------|----------------|---------|
| `200`       | `ok`           | All dependencies reachable; the instance can serve traffic. |
| `200`       | `degraded`     | Non-critical dependency is unavailable; the instance still serves traffic but with reduced functionality. |
| `503`       | `error`        | A critical dependency (e.g. the database) is unreachable; the instance should be removed from rotation. |

## Interpreting failures

- **Single `503` from one instance** — treat as instance-local. The
  orchestrator should stop routing to it and let readiness recover it. No
  paging is warranted on its own.
- **`503` across all instances at once** — indicates a shared dependency
  outage (database, network partition). This is the signal to page, because
  restarting instances will not help.
- **`degraded` responses** — the instance is intentionally kept in rotation.
  Investigate the failing sub-check listed under `checks`, but do not restart:
  a restart clears the degraded cache warm-up and makes latency worse.

## Timeouts

The probe itself has a bounded timeout. A probe that neither returns `200` nor
`503` within the timeout is treated as a failure, equivalent to `503`. Set the
orchestrator's probe timeout above the endpoint's internal check budget so a
slow-but-healthy dependency is not misread as an outage.
