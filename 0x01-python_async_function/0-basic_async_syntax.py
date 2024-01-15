#!/usr/bin/env python3
"""The basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10):
    time = random.random()*max_delay
    await asyncio.sleep(time)
    return time
