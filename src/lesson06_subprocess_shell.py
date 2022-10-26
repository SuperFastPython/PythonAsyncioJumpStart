# SuperFastPython.com
# example of running a cmd in a subprocess via the shell
import asyncio

# main coroutine
async def main():
    # run the command via shell in a subprocess
    process = await asyncio.create_subprocess_shell(
        'echo Hello World')
    # report the details of the subprocess
    print(f'subprocess: {process}')

# entry point
asyncio.run(main())
