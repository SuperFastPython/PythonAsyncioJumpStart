# SuperFastPython.com
# example of a hello world program for asyncio
import asyncio

# define a coroutine
async def custom_coroutine():
	# report a message
    print('Hello world')

# execute the coroutine
asyncio.run(custom_coroutine())
