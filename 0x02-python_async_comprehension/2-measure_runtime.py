#!/usr/bin/env python3
"""
Running multiple asynchronous comprehensions and measuring runtime.
"""


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime for executing async_comprehension
    four times in parallel.

    This function executes the async_comprehension
    coroutine four times concurrently
    using asyncio.gather, measures the total runtime,
    and returns it.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.time() - start_time

    return total_time
