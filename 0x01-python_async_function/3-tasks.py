#!/usr/bin/env python3
"""creating an asyncio task"""


import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task that runs the wait_random function
    with the given max_delay.

    Args:
        max_delay (int): The maximum allowed delay in seconds.

    Returns:
        asyncio.Task: The asyncio task created.
    """
    my_task = asyncio.create_task(wait_random(max_delay))
    return my_task
