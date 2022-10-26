# SuperFastPython.com
# example of running a coroutine from a coroutine
import asyncio

# main coroutine
async def main():
    # report a message
    print('Hello from a coroutine')
    # sleep for a moment
    await asyncio.sleep(1)

# start the coroutine program
asyncio.run(main())
