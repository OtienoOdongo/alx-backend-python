#!/usr/bin/env python3
"""asynchronous comprehension"""


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    An asynchronous list comprehension with a generator
    It collects 10 random numbers using an async comprehension
    over async_generator
    Returns:
    List[float]: The 10 random numbers
    """
    results = [x async for x in async_generator()]
    return results
