#!/usr/bin/env python3
"""1-concurrent_coroutines.py"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    values = await asyncio.gather(*tasks)
    values.sort()

    return values
