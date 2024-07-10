#!/usr/bin/env python3
""" The file executable path """

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension
""" The module executable path """


async def measure_runtime():
    beginingTime = time.time()
    await asyncio.gather(*[async_comprehension()for i in range(4)])
    endingTime = time.time()
    totalTime = endingTime - beginingTime
    return totalTime
