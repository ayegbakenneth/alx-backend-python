#!/usr/bin/env python3
""" The execution file path """

import asyncio
import random
""" This brings in the asyncio and random function """


async def wait_random(max_delay: int = 10) -> float:
    """ This function helps to generate uniform random numbers """

    generate = random.uniform(0, max_delay)
    await asyncio.sleep(generate)
    return generate
