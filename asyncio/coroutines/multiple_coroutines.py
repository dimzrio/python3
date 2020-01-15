import asyncio
import time

async def myCoro(n):
    await asyncio.sleep(1)
    print(n*2)

async def main():
    print(f"started at {time.strftime('%X')}")
    await myCoro(5)
    await myCoro(7)
    print(f"started at {time.strftime('%X')}")

asyncio.run(main())