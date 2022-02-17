import requests
import proxy_pool
import random


def request_reconn_fun(prox, ip_list, length, url, head, reconn_num, time_out):
    rand_num = random.randint(0, length - 1)
    choice = reconn_num
    while choice > 0:
        try:
            resp = requests.get(url, headers=head, proxies=prox[rand_num], timeout=time_out)
            if resp.status_code == 200:
                print(f'rand_num:{rand_num}')
                print('-------------------')
                # print(prox)
                print(f'当前使用{prox[rand_num]}访问{url}')

                print(f'第{reconn_num - choice + 1}次访问 {url}成功')
                print(f'状态码:{resp.status_code}')
                # resp.close()
                return resp.text
            else:
                print(resp.status_code)
                raise Exception('resp状态码不是200')
        except Exception as e:
            print(f'当前使用{prox[rand_num]}第{reconn_num - choice + 1}次访问{url}失败')
            print(e)
            rand_num = random.randint(1, length)
            choice -= 1
