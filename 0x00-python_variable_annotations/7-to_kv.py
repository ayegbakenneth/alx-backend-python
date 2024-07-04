#!/usr/bin/env python3
""" File execution path """
from typing import Union, Tuple
""" Attributes importation from the typing module """


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ A function that accepts str, int or float
    as an argument and return a tuple """

    a: str = k
    b: Union[int, float] = v
    c = a, + b ** 2
    return tuple(c)
