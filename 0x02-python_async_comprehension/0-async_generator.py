#!/usr/bin/env python3
import asyncio
from async_generator import async_generator

async def main():
    async for number in async_generator():
        print(number)

asyncio.run(main())

