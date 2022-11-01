# SuperFastPython.com
# example of checking the type of a coroutine

# define a coroutine
async def custom_coro():
    # do nothing
    pass

# create the coroutine
coro = custom_coro()
# check the type of the coroutine
print(type(coro))
