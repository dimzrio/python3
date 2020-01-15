import asyncio
import time

async def multiplication_task(n):
    await asyncio.sleep(1)
    return (n, n * 2)

async def main(coros):
    for future in asyncio.as_completed(coros):
        result = await future

        if result[0] == 0:
            print('Result is 0')
            continue
        
        print('Exponent from {0} is {1}'.format(result[0], result[1]))

coros = [multiplication_task(i) for i in range(10)]

asyncio.run(main(coros))
print('Task comlated')