import threading

import requests
import proxy_pool
import random
import os

# prox, ip_list, length = proxy_pool.ip_pool()


def request_reconn_fun(ind, name, fan_name, prox, ip_list, length, url, head, reconn_num, time_out):
    rand_num = random.randint(1, length)
    choice = reconn_num
    if not os.path.exists(f'./test/{name}/{fan_name}'):
        os.makedirs(f'./test/{name}/{fan_name}')
    while choice > 0:
        try:
            resp = requests.get(url, headers=head, proxies=prox[rand_num], timeout=time_out)
            if resp.status_code == 200:
                print(f'当前{threading.current_thread().getName()}使用{prox[rand_num]}访问{url} [{ind}]')
                print(f'第{reconn_num - choice + 1}次访问 {url} [{ind}]成功')
                print(f'状态码:{resp.status_code}')
                cont = resp.content
                resp.close()
                # return resp.content
                with open(f'./test/{name}/{fan_name}/{ind}.gif', 'wb') as f:
                    f.write(cont)
                print(f'第{reconn_num - choice + 1}次下载 {url} [{ind}]成功')
                break
            else:
                print(resp.status_code)
                raise Exception('网页状态码不是200')
        except Exception as e:
            print(f'当前使用{prox[rand_num]}第{reconn_num - choice + 1}次访问{url} [{ind}]失败')
            print(e)
            rand_num = random.randint(1, length)
            choice -= 1
