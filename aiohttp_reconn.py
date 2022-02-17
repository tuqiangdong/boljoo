import proxy_pool
import random
import aiohttp

prox, ip_list, length = proxy_pool.ip_pool()


async def aiohttp_reconn_fun(url, head, reconn_num, time_out):
    rand_num = random.randint(1, length)
    choice = reconn_num
    while choice > 0:
        async with aiohttp.ClientSession() as sess:
            try:
                async with sess.get(url, headers=head, proxy=proxy_pool.change_form(ip_list[rand_num])) as resp:
                    print(f'get {url}第{reconn_num - choice + 1}次成功')
                    page = await resp.text()
                    return page
            except Exception as e:
                print(f'get {url}第{reconn_num - choice + 1}次失败, 共{reconn_num}次机会')
                rand_num = random.randint(1, length)
                print(e)
                choice -= 1

        # try:
        #     print(f'当前使用{prox}访问{url}')
        #     resp = requests.get(url, headers=head, proxies=prox[rand_num], timeout=time_out)
        #     print(f'第{reconn_num - choice + 1}次访问 {url}成功')
        #     return resp.text
        # except Exception as e:
        #     print(f'第{reconn_num - choice + 1}次访问{url}失败')
        #     print(e)
        #     rand_num = random.randint(1, length)
        #     choice -= 1
