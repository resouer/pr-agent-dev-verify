# Pagination cursor handling

List endpoints return results one page at a time using an opaque cursor. Cursor
pagination is stable under concurrent writes in a way that offset pagination is
not, so it is the required mechanism for iterating large collections.

## Request and response shape

Request a page with an optional `cursor` and a `limit`:

```
GET /items?limit=100
GET /items?limit=100&cursor=eyJvZmZzZXQiOiAxMDB9
```

The response carries the current page and the cursor for the next page:

```json
{
  "items": [ ... ],
  "next_cursor": "eyJvZmZzZXQiOiAyMDB9"
}
```

## Iterating correctly

- **Start** with no cursor to get the first page.
- **Continue** by passing the `next_cursor` from the previous response verbatim.
- **Stop** when `next_cursor` is `null` (or absent). That is the only reliable
  end-of-results signal.

Do **not** stop early just because a page returned fewer than `limit` items. A
short page can occur mid-iteration (e.g. filtered rows); only a null
`next_cursor` means iteration is complete.

## Treat the cursor as opaque

The cursor is an encoded token. Callers must not decode, parse, modify, or
construct cursors. Its internal format may change without notice. Pass it back
exactly as received.

## Validity and expiry

- A cursor is tied to the query parameters of the request that produced it.
  Reusing a cursor with a **different** filter, sort, or `limit` produces an
  error, not a silently wrong page.
- Cursors may **expire**. A stale cursor returns a `400` with an
  `invalid_cursor` error. Recover by restarting iteration from the first page;
  do not retry the same expired cursor.

## Idempotency

Re-requesting the same page with the same cursor returns the same window of
results, so a client that retries after a network error can safely re-issue the
last request without skipping or duplicating items.
