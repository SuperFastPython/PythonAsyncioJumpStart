# SuperFastPython.com
# example of asynchronous generator with async for loop
import asyncio

# define an asynchronous generator
async def async_generator():
    # normal loop
    for i in range(10):
        # suspend to simulate doing work
        await asyncio.sleep(1)
        # yield the result
        yield i

# main coroutine
async def main():
    # loop over async generator with async for loop
    async for item in async_generator():
        print(item)

# execute the asyncio program
asyncio.run(main())
