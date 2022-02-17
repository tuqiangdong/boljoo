import time

import requests
import random
# url = 'http://tiqu.pyhttp.taolop.com/getip?count=500&neek=21893&type=1&yys=0&port=1&sb=&mr=1&sep=1&regions=110000,120000,130000,140000,150000,210000,370000,350000,610000,510000,500000,340000,440000,330000,430000,320000,220000,410000,640000&time=2'
# proxy_ip_pool_url = 'http://tiqu.pyhttp.taolop.com/getip?count=100&neek=21893&type=1&yys=0&port=1&sb=&mr=1&sep=1&regions=110000,120000,130000,140000,150000,210000,370000,350000,610000,510000,500000,340000,330000,440000,320000,430000,220000,410000,640000&time=2'
proxy_ip_pool_url = 'http://dps.kdlapi.com/api/getdps/?orderid=914508402276885&num=40&pt=1&sep=1'
head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}


# 构建ip代理池，默认request代理格式，返回4种数据
def ip_pool():
    prox = []
    resp = requests.get(proxy_ip_pool_url, headers=head)
    time.sleep(3)
    print('----------this is resp.text start-----------')
    print(resp.text)
    print('----------this is resp.text end-------------')
    ip_list = resp.text.split('\r\n')
    resp.close()

    for i in ip_list:
        dic = {"http": f"{i}", "https": f"{i}"}
        prox.append(dic)

    prox = prox[:-1]
    ip_list = ip_list[:-1]
    length = len(prox)
    print(f'length:{length}')
    print(prox)
    print(f'ip_list:{len(ip_list)}')
    print(ip_list)
    # rand_num = random.randint(1, length)
    return [prox, ip_list, length]


# 改变代理ip格式为async代理格式
def change_form(dic):
    result = 'http://' + dic
    print(result)
    return result


# 返回1，ip池长度的的一个随机数
def rand():
    prox, ip_list, length = ip_pool()
    rand_num = random.randint(1, length)
    return rand_num
#
# temp, ip_list, length = ip_pool()
#
# print(change_form(ip_list[5]))
