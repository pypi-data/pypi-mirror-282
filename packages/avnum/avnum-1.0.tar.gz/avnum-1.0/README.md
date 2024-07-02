# avnum

A simple Python module to calculate the average of numbers.

## Installation

```bash
pip install avnum
```

## Usage

```python
import avnum
avnum.average()
```

## Examples

Example 1:
```python
import avnum
list = [1, 2, 3]
avnum.average(list)
```

Example 2:
```python
import avnum
avnum.average(1, 2, 3)
```

Example 3:
```python
import avnum
num_input = input()
num_average = avnum.average(num_input)
print(num_average)
