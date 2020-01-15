import asyncio

async def myCoro(name):
    print('Hello, {}'.format(name))
    await asyncio.sleep(1)
    print('You learning asyncio...')

asyncio.run(myCoro('dimzrio'))