# parallel_sum.py
"""
Compute the sum of a list of numbers using Python threads.
This module demonstrates concurrent programming and thread synchronization.
"""

import threading
from typing import List


def _partial_sum(slice_: List[int], results: List[int], index: int) -> None:
    """Compute sum of a slice and store it in the results list at the given index."""
    results[index] = sum(slice_)


def parallel_sum(numbers: List[int], num_threads: int = 4) -> int:
    """Compute the sum of numbers in parallel using the specified number of threads."""
    if num_threads <= 0:
        raise ValueError("num_threads must be positive")

    n = len(numbers)
    if n == 0:
        return 0

    # Calculate chunk size using ceiling division
    chunk_size = (n + num_threads - 1) // num_threads

    results = [0] * num_threads
    threads: List[threading.Thread] = []

    for i in range(num_threads):
        start = i * chunk_size
        end = min(start + chunk_size, n)
        if start >= n:
            results[i] = 0
            continue
        thread = threading.Thread(target=_partial_sum, args=(numbers[start:end], results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(results)


if __name__ == "__main__":
    # Example usage
    numbers = list(range(1, 10001))  # Sum of numbers from 1 to 10000
    total = parallel_sum(numbers, num_threads=8)
    print(f"Sum of numbers from 1 to 10000 is {total}")
