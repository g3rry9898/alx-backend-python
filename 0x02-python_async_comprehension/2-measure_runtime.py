#!/usr/bin/env python3
import asyncio
import time
from your_previous_file import async_comprehension

async def measure_runtime():
    start_time = time.perf_counter()
    
    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    
    end_time = time.perf_counter()
    return end_time - start_time

# Example usage
async def main():
    total_runtime = await measure_runtime()
    print(f"Total runtime: {total_runtime} seconds")

# Run the example
asyncio.run(main())

