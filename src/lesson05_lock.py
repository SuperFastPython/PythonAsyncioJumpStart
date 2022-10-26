# SuperFastPython.com
# example of an asyncio mutual exclusion (mutex) lock
from random import random
import asyncio

# task coroutine with a critical section
async def task(lock, num, value):
    # acquire the lock to protect the critical section
    async with lock:
        # report a message
        print(f'>{num} got the lock, sleep for {value}')
        # block for a moment
        await asyncio.sleep(value)

# entry point
async def main():
    # create a shared lock
    lock = asyncio.Lock()
    # create many concurrent coroutines
    coros = [task(lock, i, random()) for i in range(10)]
    # execute and wait for tasks to complete
    await asyncio.gather(*coros)

# run the asyncio program
asyncio.run(main())
