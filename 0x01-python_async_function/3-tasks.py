#!/usr/bin/env python3
""" Takes int arg, waits for random delay """

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns a asyncio.Task"""
    task1 = asyncio.create_task(wait_random(max_delay))
    return task1
