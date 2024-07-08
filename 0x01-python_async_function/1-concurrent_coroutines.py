#!/usr/bin/env python3
""" File execution path """

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
""" The import modules paths """


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Function that generate sorted random numbers n number of times """

    solutions = [wait_random(max_delay) for _ in range(n)]
    resultSolution = await asyncio.gather(*solutions)
    return sorted(resultSolution)
