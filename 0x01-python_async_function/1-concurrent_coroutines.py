#!/usr/bin/env python3
""" Takes int arg, waits for random delay """

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn task_wait_random n times with the specified max_delay
    return listof all the delays in ascending order
    """
    result_list: List = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    result_list = await asyncio.gather(*tasks)
    for i in range(len(result_list)):
        for j in range(i + 1, len(result_list)):
            if result_list[j] < result_list[i]:
                tmp = result_list[j]
                result_list[j] = result_list[i]
                result_list[i] = tmp

    return result_list
