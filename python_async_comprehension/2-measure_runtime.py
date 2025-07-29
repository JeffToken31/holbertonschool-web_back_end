#!/usr/bin/env python3
"""
Function measuring execution time
of coroutine and return average of duration
"""
from typing import List
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Function measuring execution time
    of coroutine and return average of duration
    """
    start: float = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end: float = time.time()

    duration: float = end - start
    return duration
