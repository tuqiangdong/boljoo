import asyncio
import time

import blog_spider
import aiohttp

# 控制并发度，同时运行不超过10个
sema = asyncio.Semaphore(10)



async def async_spi(url):
    async with sema:
        async with aiohttp.ClientSession() as sess:
            async with sess.get(url) as resp:
                text = await resp.text()
                print(f'{url}: {len(text)}')


loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(async_spi(i))
    for i in blog_spider.urls
]
st = time.time()
loop.run_until_complete(asyncio.wait(tasks))
en = time.time()
print(en - st)