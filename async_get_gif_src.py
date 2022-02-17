import asyncio
import aiohttp
import aiohttp_reconn
import queue
import get_btn
from lxml import etree
import get_btn

q = queue.Queue()
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

test_url = 'http://www.boljoo.com/4107.html'


def parse(resp_text):
    html = etree.HTML(resp_text)
    src_value = html.xpath('//*[@id="primary-home"]/article/div[1]/p[2]/img/@src')[0]
    print(src_value)
    return src_value


async def get_all_gif_url(url, share_q: queue.Queue):
    total = get_btn.get_btn_amount(url)
    for i in range(1, total + 1):
        temp = url + f'/{i}'
        # print('---------------')
        # print(temp)
        resp_text = await aiohttp_reconn.aiohttp_reconn_fun(temp, head, 3, 45)
        src_value = parse(resp_text)
        q.put(src_value)



async def main():
    total = get_btn.get_btn_amount(test_url)
    tasks = [
        asyncio.create_task(get_all_gif_url(test_url, q,))
        for i in range(1, total + 1)
    ]
    await asyncio.wait(tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

for i in range(0, q.qsize()):
    print(q.get())
