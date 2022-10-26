# SuperFastPython.com
# example of adding a done callback function to a task
import asyncio

# custom done callback function
def handle(task):
    print(f'Task callback done: {task.done()}')

# define a coroutine for a task
async def task_coroutine():
    # report a message
    print('executing the task')
    # block for a moment
    await asyncio.sleep(1)

# custom coroutine
async def main():
    # report a message
    print('main coroutine')
    # create and schedule the task
    task = asyncio.create_task(task_coroutine())
    # add a done callback function
    task.add_done_callback(handle)
    # wait for the task to complete
    await task

# start the asyncio program
asyncio.run(main())
