#!/usr/bin/env python3
"""
Function takes a list of sequence typing with any and
return an optionnal containing tyoe any
"""
from typing import Sequence, Optional, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Function takes a list of sequence typing with any and
    return an optionnal containing tyoe any
    """
    if lst:
        return lst[0]
    else:
        return None
