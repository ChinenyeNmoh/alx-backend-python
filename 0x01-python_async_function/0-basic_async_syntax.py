#!/usr/bin/env python3
""" Takes int arg, waits for random delay """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Waits for random delay between 0 and max_delay, returns that """
    time_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(time_delay)
    return time_delay
