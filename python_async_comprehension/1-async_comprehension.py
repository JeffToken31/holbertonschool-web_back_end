#!/usr/bin/env python3
"""
Coroutin collecte 10 random numbers with use of list comprehension
and return list
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Coroutin collecte 10 random numbers with use of list comprehension
    and return list
    """
    results: List[float] = []
    async for i in async_generator():
        results.append(i)
    return results
