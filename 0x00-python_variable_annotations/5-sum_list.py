#!/usr/bin/env python3

from typing import List
""" Importing the attribute list from typing module"""


def sum_list(input_list: List[float]) -> float:
    """ Function that recieve a float list and return a float sum"""
    t_sum = 0.0
    for value in input_list:
        t_sum += value
    return t_sum
