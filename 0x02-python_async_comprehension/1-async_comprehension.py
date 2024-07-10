#!/usr/bin/env python3
""" File executable path """

import asyncio
async_generator = __import__('0-async_generator').async_generator
""" The modules import path """


async def async_comprehension():
    """ This function make use of async_generator
    function result """

    resultList = [await value async for value in async_generator()]
    return resultList
