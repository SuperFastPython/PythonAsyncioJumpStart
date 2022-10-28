# SuperFastPython.com
# example of wait/notify with an asyncio condition
import asyncio

# task coroutine
async def task(condition, work_list):
    # suspend for a moment
    await asyncio.sleep(1)
    # add data to the work list
    work_list.append(33)
    # notify a waiting coroutine that the work is done
    print('Task sending notification...')
    async with condition:
        condition.notify()

# main coroutine
async def main():
    # create a condition
    condition = asyncio.Condition()
    # prepare the work list
    work_list = []
    # wait to be notified that the data is ready
    print('Main waiting for data...')
    async with condition:
        # create and start the task
        _ = asyncio.create_task(
            task(condition, work_list))
        # wait to be notified
        await condition.wait()
    # we know the data is ready
    print(f'Got data: {work_list}')

# run the asyncio program
asyncio.run(main())
