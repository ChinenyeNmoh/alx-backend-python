#!/usr/bin/env python3
""" 2-measure_runtime.py file (task 2)"""
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime function. Add doc later"""
    start_time = time.time()
    p1 = async_comprehension()
    p2 = async_comprehension()
    p3 = async_comprehension()
    p4 = async_comprehension()
    await asyncio.gather(p1, p2, p3, p4)
    end_time = time.time()
    return end_time - start_time
