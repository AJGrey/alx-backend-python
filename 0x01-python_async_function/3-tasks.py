#!/usr/bin/env python3
import asyncio
from typing import Union
from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Creates and returns an asyncio.Task for wait_random"""
    
    task = create_task(wait_random(max_delay))
    return task
