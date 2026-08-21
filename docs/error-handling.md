# Error handling

`calc-demo` distinguishes between the kinds of errors it raises so callers can
handle them deliberately.

## Error categories

- **Validation errors** (`ValueError`) — raised for malformed input, such as a
  non-numeric argument or a `running_total` list containing a `None`. These are
  the caller's responsibility to fix and are never retried.
- **Domain errors** (`ZeroDivisionError`) — raised for mathematically undefined
  operations, e.g. `percent(1, 0)`. Callers should guard against these before
  calling.
- **Unexpected errors** — any other exception is a bug in the library and should
  be reported.

## Principles

- **Fail fast:** invalid input raises immediately rather than producing a
  silently wrong result.
- **Preserve context:** wrapped exceptions use `raise ... from` so the original
  cause is retained in the traceback.
- **No silent defaults:** the library never substitutes a fallback value for
  bad input; the caller decides how to recover.

## Recommended pattern

```python
try:
    percent(numerator, denominator)
except ZeroDivisionError:
    # handle the undefined case explicitly
    ...
except ValueError:
    # surface the input problem to the user
    ...
```
