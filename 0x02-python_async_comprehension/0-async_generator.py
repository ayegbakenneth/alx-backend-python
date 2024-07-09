#!/usr/bin/env python3
""" File executable path """

import asyncio
import random
""" Import module path """


async def async_generator():
    """ An async generator function that wait 1 second,
    then yield a random number between 0 and 10 """

    for i in range(10):
        await asyncio.sleep(1)
        result = random.randint(0, 10)
        yield result
