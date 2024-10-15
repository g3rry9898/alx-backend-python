#!/usr/bin/env python3
import asyncio
import random

# Assuming async_generator is defined as follows:
async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

# Define the async_comprehension coroutine
async def async_comprehension():
    # Collect 10 random numbers using an async comprehension
    return [number async for number in async_generator()]

# Example usage
async def main():
    result = await async_comprehension()
    print(result)

# Run the example
asyncio.run(main())

