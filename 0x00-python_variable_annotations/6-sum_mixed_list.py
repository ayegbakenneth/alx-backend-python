#!/usr/bin/env python3
""" File execution path """
from typing import List, Union
""" File importation from module """


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Function that accept mixed list and return float sum """
    return sum(mxd_lst)
