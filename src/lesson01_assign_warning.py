# SuperFastPython.com
# example of creating but not awaiting a coroutine

# define a coroutine
async def custom_coroutine():
	# report a message
    print('Hello world')

# create the coroutine and assign it to a variable
coro = custom_coroutine() # raises warning
