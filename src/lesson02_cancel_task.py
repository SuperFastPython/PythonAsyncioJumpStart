# SuperFastPython.com
# example of canceling an asyncio task
import asyncio

# define a coroutine for a task
async def task_coroutine():
    # report a message
    print('executing the task')
    # suspend for a moment
    await asyncio.sleep(1)

# custom coroutine
async def main():
    # report a message
    print('main coroutine')
    # create and schedule the task
    task = asyncio.create_task(task_coroutine())
    # wait a moment
    await asyncio.sleep(0.5)
    # cancel the task
    was_cancelled = task.cancel()
    print(f'>was canceled: {was_cancelled}')
    # wait a moment
    await asyncio.sleep(0.1)
    # report the status
    print(f'>canceled: {task.cancelled()}')

# start the asyncio program
asyncio.run(main())
