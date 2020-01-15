import asyncio

async def myTask(name):
    await asyncio.sleep(1)
    print('Hello, {0}...'.format(name))
    
async def main():
    task1 = asyncio.create_task(myTask('kareem'))
    task2 = asyncio.create_task(myTask('asiyah'))

    await task1
    await task2

    if task1.done() and task2.done:
        print("Welcome to the world...")

asyncio.run(main())