#!/usr/bin/env python3
""" write a measure_runtime coroutine that will
execute async_comprehension four times in parallel using asyncio.gather"""
import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure_runtime should measure the total runtime and return it."""
    start = perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = perf_counter()
    total_time = end - start
    return total_time
