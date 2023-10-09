#!/usr/bin/env python3
"""Measuring the runtime of wait_n function"""


import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return total_time / n.

    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): The maximum allowed delay in seconds.

    Returns:
        float: Average execution time per call to wait_n.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time

    return total_time / n

    if __name__ == "__main__":
        n = 5
        max_delay = 9
        print(measure_time(n, max_delay))
