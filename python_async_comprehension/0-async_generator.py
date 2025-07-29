#!/usr/bin/python3
"""
Function genrator yield a ramdom number waiting 1 sec ten times
"""
import random
from typing import AsyncGenerator
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Function genrator yield a ramdom number waiting 1 sec ten times
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
