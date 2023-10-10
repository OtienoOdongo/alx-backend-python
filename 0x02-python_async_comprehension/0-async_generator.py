#!/usr/bin/env python3
"""python asynchronous generator"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random numbers between 0 and 10.

    This coroutine loops 10 times, asynchronously waiting for
    1 second in each iteration,
    and then yields a random float between 0 and 10.

    Yields:
        float: A random float between 0 and 10 on each iteration.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
