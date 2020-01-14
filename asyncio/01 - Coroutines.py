import asyncio
import random

async def task(id):
    process_time = random.randint(1, 5)
    await asyncio.sleep(process_time)
    print("Coroutine-{0}: has successfully completed after {1} seconds".format(id, process_time))

async def main():
    tasks = []

    for id in range(10):
        tasks.append(asyncio.ensure_future(task(id)))
    
    await asyncio.gather(*tasks)

asyncio.run(main())