#!/usr/bin/python3
"""
Function genrator yield a ramdom number wai0ingt 1 sec ten times
"""
import random
from typing import AsyncGenerator
import asyncio

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Function genrator yield a ramdom number wai0ingt 1 sec ten times
    """
    for _ in range(10):
        yield random.random()
        await asyncio.sleep(1)
        