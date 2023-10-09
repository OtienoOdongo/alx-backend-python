#!/usr/bin/env python3
"""modifying a function"""


import asyncio
from typing import List
from asyncio import Task

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): The maximum allowed delay in seconds.

    Returns:
        List[float]: List of delays (float values) in ascending order.
    """
    tasks: List[Task] = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    await asyncio.gather(*tasks)
    return sorted(task.result() for task in tasks)

if __name__ == "__main__":
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
