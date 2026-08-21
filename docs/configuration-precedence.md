# Configuration precedence

`calc-demo` resolves configuration from several sources. When the same setting
is defined in more than one place, later sources in this list win:

1. **Built-in defaults** — compiled into the library.
2. **Config file** — values from `calc.toml` in the project root.
3. **Environment variables** — any `CALC_*` variable overrides the config file.
4. **Explicit arguments** — values passed directly to a function call take
   precedence over everything else.

## Example

Given a `calc.toml` that sets `precision = 2` and an environment variable
`CALC_PRECISION=4`, a call to `percent(1, 3, precision=6)` uses `6`, because the
explicit argument outranks both the environment variable and the config file.

## Notes

- Precedence is evaluated per-setting, not per-source: a value taken from the
  config file for one setting does not prevent an environment variable from
  overriding a different setting.
- Unset sources are skipped entirely; they never reset a value back to its
  default.
