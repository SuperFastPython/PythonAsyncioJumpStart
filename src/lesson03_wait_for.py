# SuperFastPython.com
# example of waiting for a coroutine with a timeout
from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro():
    # generate a random value between 0 and 1
    value = 1 + random()
    # report message
    print(f'>task got {value}')
    # suspend for a moment
    await asyncio.sleep(value)
    # report all done
    print('>task done')

# main coroutine
async def main():
    # create a task
    task = task_coro()
    # execute and wait for the task without a timeout
    try:
        await asyncio.wait_for(task, timeout=0.2)
    except asyncio.TimeoutError:
        print('Gave up waiting, task canceled')

# start the asyncio program
asyncio.run(main())
