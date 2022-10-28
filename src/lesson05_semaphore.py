# SuperFastPython.com
# example of using an asyncio semaphore
from random import random
import asyncio

# task coroutine
async def task(semaphore, number):
    # acquire the semaphore
    async with semaphore:
        # generate a random value between 0 and 1
        value = random()
        # suspend for a moment
        await asyncio.sleep(value)
        # report a message
        print(f'Task {number} got {value}')

# main coroutine
async def main():
    # create the shared semaphore
    semaphore = asyncio.Semaphore(2)
    # create and schedule tasks
    tasks = [asyncio.create_task(task(semaphore, i))
        for i in range(10)]
    # wait for all tasks to complete
    _ = await asyncio.wait(tasks)

# start the asyncio program
asyncio.run(main())
