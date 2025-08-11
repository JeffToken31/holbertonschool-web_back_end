#!/usr/bin/env python3
"""
Function about pagination
return a tuple size two: a page starting and how much elements by page
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of page asked and size of page
    """
    start: int = page * page_size - page_size
    still: int = start + page_size
    return (start, still)
