# SuperFastPython.com
# example of using an asyncio event object
from random import random
import asyncio

# task coroutine
async def task(event, number):
    # wait for the event to be set
    await event.wait()
    # generate a random value between 0 and 1
    value = random()
    # suspend for a moment
    await asyncio.sleep(value)
    # report a message
    print(f'Task {number} got {value}')

# main coroutine
async def main():
    # create a shared event object
    event = asyncio.Event()
    # create and run the tasks
    tasks = [asyncio.create_task(task(event, i))
        for i in range(5)]
    # allow the tasks to start
    print('Main suspending...')
    await asyncio.sleep(0)
    # start processing in all tasks
    print('Main setting the event')
    event.set()
    # await for all tasks  to terminate
    _ = await asyncio.wait(tasks)

# run the asyncio program
asyncio.run(main())
