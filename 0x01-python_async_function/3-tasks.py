#!/usr/bin/env python3
import asyncio
from typing import Union
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Union[Task, None]:
    """Creates and returns an asyncio.Task for wait_random"""
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
