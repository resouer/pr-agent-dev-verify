# Cache invalidation behavior

Cached reads make the service fast, but a cache is only correct if stale entries
are removed promptly and predictably. This document describes when and how
cached data becomes invalid.

## What is cached

Read responses are cached keyed by the resource identity and the parameters
that affect the result. Two requests that would produce the same response share
a cache entry; requests that differ in any result-affecting parameter do not.

## How entries expire

- **Time-to-live (TTL).** Every entry has a TTL. After it elapses the entry is
  considered stale and the next read repopulates it from the source of truth.
- **Write-through invalidation.** A write that changes a resource invalidates
  the affected cache entries as part of the write, so a read immediately after
  a successful write reflects the new value rather than waiting for the TTL.
- **Explicit purge.** An entry can be dropped on demand (for example after an
  out-of-band data fix). A purge removes the entry; the next read rebuilds it.

## Consistency guarantees

- **Read-your-writes** holds for a client that made the write: once the write
  returns success, that client's subsequent reads see the new value.
- Across clients, propagation is bounded by the TTL. A reader that did not make
  the write may briefly see the previous value until the entry is invalidated
  or expires.
- Invalidation removes entries; it does not pre-populate them. The first read
  after invalidation pays the cost of rebuilding the entry (a cache miss).

## Ordering and races

- Invalidation is tied to the write it belongs to. If a write and a concurrent
  read race, the read either sees the pre-write value (and its entry is then
  invalidated) or the post-write value; it never caches a value that was never
  the source-of-truth state.
- Do not invalidate *before* the write commits. Invalidating early lets a
  concurrent read repopulate the cache with the old value, which then survives
  until the TTL and reintroduces the staleness the invalidation was meant to
  fix.

## Operational notes

- A rise in cache misses immediately after a deploy or bulk purge is expected;
  the cache warms back up as reads repopulate it.
- Lowering the TTL narrows the staleness window but increases load on the source
  of truth. Tune it against how tolerant callers are of brief staleness.
