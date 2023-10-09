#!/usr/bin/env python3
"""
python async function that generates random numbers
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that generates a random delay
    between 0 and max_delay (inclusive) seconds.

    Args:
        max_delay (int):
        The maximum allowed delay in seconds (default is 10).

    Returns:
        float:
        The generated random delay in seconds.
    """
    rnd = random.uniform(0, max_delay)
    await asyncio.sleep(rnd)
    return rnd


async def main():
    """
    Main asynchronous function that demonstrates the usage of wait_random.
    """
    rnd_delay = await wait_random()
    print(rnd_delay)


if __name__ == "__main__":
    asyncio.run(main())
