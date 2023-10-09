#!/usr/bin/env python3
"""Running multiple tasks simultaneously"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum allowed delay in seconds.

    Returns:
        List[float]: List of delays (float values) in ascending order.
    """
    tasks = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    await asyncio.gather(*tasks)
    return sorted(task.result() for task in tasks)


async def main():
    sorted_delays = await wait_n(n, max_delay)
    print(sorted_delays)

if __name__ == "__main__":
    asyncio.run(main())
