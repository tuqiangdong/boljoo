import asyncio
import queue

import aiohttp
import request_reconn_binary
import os
import requests
import aiofiles
import proxy_pool
import random

head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}


# def download_gif_fun(src, seq, name, fan_name, gif_q: queue.Queue):
#
#     if not os.path.exists(f'./test/{name}/{fan_name}'):
#         os.makedirs(f'./test/{name}/{fan_name}')
#     with ThreadPoolExecutor() as t:
#         for i in range(1, gif_q.qsize()+1):
#             t.submit(request_reconn_binary.request_reconn_fun, src, head, 3, 45)
#             binary = request_reconn_binary.request_reconn_fun(src, head, 3, 45)
#             with open(f'./test/{name}/{fan_name}/{seq}.gif') as f:
#                 f.write(binary)
# def get_binary(binary_content, name, fan_name, seq):
#     if not os.path.exists(f'./test/{name}/{fan_name}'):
#          os.makedirs(f'./test/{name}/{fan_name}')
#     with open(f'./test/{name}/{fan_name}/{seq}.gif') as f:
#         f.write(binary_content)
#
#
# def mutil_thread(src, seq, name, fan_name, gif_q: queue.Queue):
#     l1 = []
#     for i in range(0, gif_q.qsize()):
#         l1.append(i)
#     with ThreadPoolExecutor() as t:

# 异步写入f'./test/{name}/{fan_name}/*.gif'
# reconn为重连次数
async def down_gif(prox, ip_list, length, src, name, fan_name, reconn_num, time_out, seq):
    # list1 = []
    # for i in range(0, gif_q.qsize()):
    #     list1.append(gif_q.get())
    # prox, ip_list, length = proxy_pool.ip_pool()
    # for i in list1:
    rand_num = random.randint(0, length - 1)
    choice = reconn_num
    while choice > 0:
        async with aiohttp.ClientSession() as sess:
            try:
                print(f'当前使用{proxy_pool.change_form(ip_list[rand_num])}第{reconn_num-choice+1}次访问{fan_name}无序的第{seq}个gif')
                async with sess.get(src, headers=head, proxy=proxy_pool.change_form(ip_list[rand_num]), timeout=time_out) as resp:
                    print(await resp.read())
                    if not os.path.exists(f'./test/{name}/{fan_name}'):
                        os.makedirs(f'./test/{name}/{fan_name}')
                    async with aiofiles.open(f'./test/{name}/{fan_name}/{seq}.gif', 'wb') as f:
                        print('enter write')
                        await f.write(await resp.content.read())
                        print(f'第{reconn_num - choice + 1}次下载{src}成功')
            except Exception as e:
                print(f'第{reconn_num - choice + 1}次下载{src}失败')
                rand_num = random.randint(0, length - 1)
                choice -= 1


async def main(prox, ip_list, length, name, fan_name, reconn_num, time_out, list1):

    # tasks = [
    #     asyncio.create_task(down_gif(src, name, fan_name, reconn_num, time_out, list1.index(src) + 1))
    #     for src in list1
    # ]
    # for src in list1:
    #     print('-------------in list1---------------')
    #     print(src)
    #     tasks.append(asyncio.create_task(down_gif(prox, ip_list, length, src, name, fan_name, reconn_num, time_out, list1.index(src) + 1)))
    #
    tasks = [
        asyncio.create_task(down_gif(prox, ip_list, length, src, name, fan_name, reconn_num, time_out, list1.index(src)+1))
        for src in list1
    ]
    await asyncio.wait(tasks)
    # return tasks

