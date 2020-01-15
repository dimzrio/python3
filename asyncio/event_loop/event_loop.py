import asyncio

async def coro01():
    while True:
        await asyncio.sleep(1)
        print("This is coroutines 1")

async def coro02():
    while True:
        await asyncio.sleep(2)
        print("This is coroutines 2")

loop = asyncio.get_event_loop()

try:
    asyncio.ensure_future(coro01())
    asyncio.ensure_future(coro02())

    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    loop.close()