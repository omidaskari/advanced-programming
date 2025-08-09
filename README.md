# Advanced Programming

This repository contains bachelor-level projects that illustrate advanced programming techniques such as concurrency and algorithm optimization.

## Contents

- **`parallel_sum.py`** – A Python script that uses the `threading` module to compute the sum of a list of integers in parallel. It demonstrates dividing work across multiple threads and combining partial results.

## Running the example

To run the example script, clone or download the repository and execute it with Python 3:

```bash
python3 parallel_sum.py
```

The script will compute the sum of numbers from 1 to 10,000 using eight threads and print the result. You can also import the `parallel_sum` function in your own code:

```python
from parallel_sum import parallel_sum

numbers = [1, 2, 3, 4, 5]
result = parallel_sum(numbers, num_threads=2)
print(result)  # Outputs 15
```

## Notes

These examples are simplified for educational purposes. For more sophisticated concurrency, you might explore Python's `multiprocessing` module or asynchronous programming with `asyncio`.
