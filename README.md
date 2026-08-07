# calc-demo

A tiny calculator library used to exercise the IntentLab Pull Request Agent on dev.

## Installation

Install the package in editable mode from the project root:

```bash
pip install -e .
```

## Usage

```python
from calc.calc import percent
percent(1, 4)  # 25.0
```

### running_total

`running_total` takes a list of numbers and returns the cumulative sum at each
position:

```python
from calc.calc import running_total
running_total([1, 2, 3, 4])  # [1.0, 3.0, 6.0, 10.0]
```
QA marker: panel TTL verification 2026-08-07 (202721)
