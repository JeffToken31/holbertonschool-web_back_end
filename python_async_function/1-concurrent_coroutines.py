#!/usr/bin/env python3
"""
Coroutin that takes in an integer argument
(max_delay, with a default value of 10)
named wait_random that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutin which take argument and
    return delay awaiting to launch this function
    """
    results: List = []
    for _ in range(n):
        results.append(await wait_random(max_delay))
    results.sort()
    return results
