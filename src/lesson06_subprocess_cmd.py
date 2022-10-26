# SuperFastPython.com
# example of running a command in a subprocess directly
import asyncio

# main coroutine
async def main():
    # run the command in a subprocess
    process = await asyncio.create_subprocess_exec(
        'echo', 'Hello World')
    # report the details of the subprocess
    print(f'subprocess: {process}')

# entry point
asyncio.run(main())
