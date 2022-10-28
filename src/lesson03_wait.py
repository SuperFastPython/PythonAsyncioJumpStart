# SuperFastPython.com
# example of waiting for all tasks to complete
from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random()
    # suspend for a moment
    await asyncio.sleep(value)
    # report the value
    print(f'>task {arg} done with {value}')

# main coroutine
async def main():
    # create many tasks
    tasks = [asyncio.create_task(task_coro(i))
        for i in range(10)]
    # wait for all tasks to complete
    _ = await asyncio.wait(tasks)
    # report results
    print('All done')

# start the asyncio program
asyncio.run(main())
