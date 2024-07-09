#!/usr/bin/env python3
""" File executable path """

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n
""" Import modules path """


async def measure_time(n: int, max_delay: int) -> float:
    """ Function that measures its total execution time """

    beginnerTime = time.time()
    result = wait_n(n, max_delay)
    await asyncio.sleep(result)
    endingTime = time.time()
    totalTime = endingTime - beginnerTime
    averageTime = totalTime / n
    return averageTime
