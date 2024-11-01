#!/usr/bin/env python3
"""
This module provides a coroutine that asynchronously generates random numbers.
"""

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """
    Loop 10 times, each time asynchronously wait 1 second, then yield a random number
    between 0 and 10.

    :return: An asynchronous generator yielding random numbers.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

# Example usage
if __name__ == "__main__":
    async def main():
        async for number in async_generator():
            print(number)

    asyncio.run(main())

