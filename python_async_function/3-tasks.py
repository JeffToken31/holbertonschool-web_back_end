#!/usr/bin/env python3
"""
Function that return a asyncio task object
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """
    Function that return a asyncio task object
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
