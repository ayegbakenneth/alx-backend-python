#!/usr/bin/env python3
""" File executable path """

from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random
""" Modules import path """


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Function that generate sorted random numbers n number of times """

    solutions = [task_wait_random(max_delay) for _ in range(n)]
    resultSolution = await asyncio.gather(*solutions)
    return sorted(resultSolution)
