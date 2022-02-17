import asyncio
import aiohttp_reconn
import get_all_fan_url
import queue

head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
url = 'http://www.boljoo.com/tag/%e9%a5%ad%e5%86%88%e5%8a%a0%e5%a5%88%e5%ad%90'

# q = queue.Queue()
# url_list, fan_sum = get_all_fan_url.get_all_fan(url)
# loop = asyncio.get_event_loop()
# tasks = [
#     loop.create_task(aiohttp_reconn.aiohttp_reconn_fun(i))
#     for i in url_list
# ]
# loop.run_until_complete(asyncio.wait(tasks))
