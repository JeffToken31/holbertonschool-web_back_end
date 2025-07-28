#!/usr/bin/env python3
"""
Function that takes a string k and an int OR float
v as arguments and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float
v and k should be annotated as a float
"""
from typing import Tuple


def to_kv(k: str, v: float | int) -> Tuple[str, float]:
    """
    Function that takes a string k and an int OR float
    v as arguments and returns a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float
    v and k should be annotated as a float
    """
    return (k, float(v ** 2))
