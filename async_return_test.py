import asyncio
import queue
import random


async def double(num, share_q: queue.Queue):
    # await asyncio.sleep(1)
    # await asyncio.sleep(random.randint(1, 3))
    res = num * 2
    share_q.put(res)


q = queue.Queue()
list1 = [1, 3, 5, 8]


# 一个元素的返回
# loop = asyncio.get_event_loop()
# get_future = asyncio.ensure_future(double(list1[1]))
# loop.run_until_complete(get_future)
# print(get_future.result())

async def main():
    tasks = [
        asyncio.create_task(double(i, q))
        for i in list1
    ]
    await asyncio.wait(tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
# print(q.get())
print(q.qsize())
for i in range(0, q.qsize()):
    print(q.get())
# 一个元素的返回 callback
# loop = asyncio.get_event_loop()
# task = loop.create_task((double(list1[1])))
# # get_future = asyncio.ensure_future(double(list1[1]))
# task.add_done_callback(callback)
# # loop.run_until_complete(get_future)
# loop.run_until_complete(task)
# print(task.result())

# 一堆元素的返回
# loop = asyncio.get_event_loop()
# tasks = [
#     asyncio.create_task(double(i))
#     for i in list1
# ]
# loop.run_until_complete(await asyncio.wait(tasks))
# print(tasks.result())

# 一堆元素的返回 callback
# loop = asyncio.get_event_loop()
# tasks = []
# for i in list1:
#     temp = asyncio.create_task(double(list1[i]))
#     temp.add_done_callback(callback)
#     tasks.append(temp)
# # get_future = asyncio.ensure_future(double(list1[1]))
# # tasks.add_done_callback(callback)
# # loop.run_until_complete(get_future)
# loop.run_until_complete(tasks)
# print(tasks.pop())
