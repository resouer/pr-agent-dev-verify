# Usage Examples

A couple of quick examples for getting started.

## Example 1: Basic invocation

```bash
pr-agent-dev-verify --input ./data.json --out ./result.json
```

Reads `data.json`, processes it, and writes the result to `result.json`.

## Example 2: Streaming from stdin

```bash
cat data.json | pr-agent-dev-verify --stdin --format table
```

Pipes input on stdin and renders the output as a formatted table.
