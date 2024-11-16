import asyncio
import time

import aiohttp
import requests


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.status)


async def fetch_with_blocking(url):
    resp = requests.get(url)
    print(resp.status_code)


async def foo1(x):

    print(x**2)
    await asyncio.sleep(1)
    print("foo1 sleep 2")
    await asyncio.sleep(1)

    print("foo1 завершена")


async def foo2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print("foo2 завершена")


async def main():
    task1 = asyncio.create_task(foo1(4))
    task2 = asyncio.create_task(foo2(4))

    await task1
    task2


start_time = time.time()
print(f"start time = {start_time}")
asyncio.run(main())

print(f"finish time = {time.time() - start_time}")


# async def main():
#     urls = [
#         'https://www.google.com'
#     ] * 10

#     tasks = [fetch(url) for url in urls]
#     await asyncio.gather(*tasks)


# start_time = time.time()
# print(f"start time = {start_time}")
# asyncio.run(main())

# print(f"finish time = {time.time() - start_time}")
