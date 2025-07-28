#!/usr/bin/env python3
"""
Funtion which takes a list input_list of floats
as argument and returns their sum as a float
"""


def sum_list(input_list: list[float]) -> float:
    """
    Funtion which takes a list input_list of floats
    as argument and returns their sum as a float
    """
    result: float = 0.00
    for number in input_list:
        result += number
    return result
