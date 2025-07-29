#!/usr/bin/env python3
"""
Coroutin that takes in an integer argument
(max_delay, with a default value of 10)
named wait_random that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Not my code impossible to find ressource
    """
    delays: float = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
