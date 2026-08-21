# Graceful shutdown expectations

When an instance is asked to stop — during a deploy, a scale-down, or a node
drain — it must drain in-flight work before exiting so that no client sees a
dropped request.

## Shutdown sequence

1. **Signal received.** The process receives `SIGTERM`. This is the request to
   begin shutdown, not an order to exit immediately.
2. **Fail readiness.** The instance immediately begins returning a non-ready
   status from its readiness probe so the load balancer stops sending new
   requests. It keeps serving requests already in flight.
3. **Drain.** In-flight requests are allowed to complete up to the drain
   deadline. New connections are refused once the load balancer has removed the
   instance.
4. **Flush.** Buffered work — metrics, logs, queued writes — is flushed.
5. **Exit.** The process exits `0` once draining and flushing complete, or when
   the drain deadline is reached, whichever comes first.

## Deadlines

- The drain deadline must be **shorter** than the orchestrator's termination
  grace period. If draining outlasts the grace period the orchestrator sends
  `SIGKILL`, which skips the flush step and can drop in-flight work.
- A recommended margin is: `drain deadline = grace period − flush budget`, so
  there is always time to flush after the last request completes.

## What callers should expect

- Requests accepted before `SIGTERM` complete normally.
- Requests arriving after readiness starts failing are routed to another
  instance by the load balancer; the shutting-down instance does not accept
  them.
- A client should never need to retry solely because of a graceful shutdown.
  If clients see connection resets during deploys, the drain deadline is likely
  too short or readiness is not failing early enough.
