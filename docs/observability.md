# Observability

`calc-demo` emits signals so its behavior can be understood in production
without attaching a debugger.

## Logging

- Logs use the standard `logging` module under the `calc` logger namespace, so
  applications can configure levels and handlers centrally.
- Each log record includes the operation name and the arguments it was called
  with (excluding anything marked sensitive).
- The library never calls `print`; all diagnostics go through the logger.

## Metrics

The following metrics are exposed for each public operation:

- **Call count** — total invocations, tagged by operation.
- **Error count** — failures, tagged by operation and error category.
- **Latency** — duration histogram, so slow calls are visible at the tail.

## Tracing

When a tracer is configured, each operation runs inside its own span. Spans
carry the operation name and outcome (`ok` / `error`) as attributes and nest
under the caller's active span, so a single request can be followed end to end.

## Correlation

A request or correlation id, when supplied by the caller, is attached to every
log line, metric, and span for that call, so signals from the three subsystems
can be joined for a single operation.
