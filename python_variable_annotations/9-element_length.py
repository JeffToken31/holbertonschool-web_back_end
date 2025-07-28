#!/usr/bin/env python3
"""
Function takes a list of sequence and
return list of tuple containing sequence and int
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function takes a list of sequence and
    return list of tuple containing sequence and int
    """
    return [(i, len(i)) for i in lst]
