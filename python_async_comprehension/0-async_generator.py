#!/usr/bin/env python3
"""
Asynchronous generator that yields a random float between 0 and 10,
after waiting 1 second, repeated 10 times.
"""
import random
from typing import Generator, Any
import asyncio


async def async_generator() -> Generator[float, Any, Any]:
    """
    Asynchronous generator that yields a random float between 0 and 10,
    after waiting 1 second, repeated 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
