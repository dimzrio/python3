import asyncio

async def multiplication(n):
    await asyncio.sleep(1)
    print('Multiplication {0} x 2 is {1}'.format(n, n * 2))

async def main():
    await asyncio.ensure_future(multiplication(1))
    await asyncio.ensure_future(multiplication(2))
    await asyncio.ensure_future(multiplication(3))

asyncio.run(main())