# SuperFastPython.com
# example of calling a coroutine directly

# define a coroutine
async def custom_coroutine():
	# report a message
    print('Hello world')

# call the coroutine directly
custom_coroutine() # raises warning
