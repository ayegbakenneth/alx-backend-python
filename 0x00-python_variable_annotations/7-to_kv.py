#!/usr/bin/env python3
""" File execution path """
from typing import List, Union, Tuple
""" Attributes importation from the typing module """


def to_kv(k: str, num: Union[int, float]) -> Tuple[str, float]:
    """ A function that accepts str, int or float
    as an argument and return a tuple """

    a: str = k
    b: Union[int, float] = num
    c = a, + b ** 2
    return tuple(c)
