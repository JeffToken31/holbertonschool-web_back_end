#!/usr/bin/env python3
"""
Function takes a mapping, any and union of T and any
to return union of any, T
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')
def safely_get_value(dct: Mapping, key: Any, default: Union[T, Any] = None) -> Union[Any, T]:
    """
    Function takes a mapping, any and union of T and any
    to return union of any, T
    """
    if key in dct:
        return dct[key]
    else:
        return default