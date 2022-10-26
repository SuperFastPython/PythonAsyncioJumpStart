# SuperFastPython.com
# example of running a coroutine
import asyncio

# main coroutine
async def main():
    # report a message
    print('Hello from a coroutine')

# start the coroutine program
asyncio.run(main())
