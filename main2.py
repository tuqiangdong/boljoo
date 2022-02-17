
from thred_pool_get_all_gif_src import get_gif_list
import time
import is_exist
import winsound
import request_reconn_binary
from concurrent.futures import ThreadPoolExecutor
import get_pool
import yue


head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
url = 'http://www.boljoo.com/4288.html'


def m(url):
    prox, ip_list, length = get_pool.get_pool_list()
    # fout = open('./ip.txt', 'r')
    # prox, ip_list, length = yue.ddd(fout)
    start = time.time()
    print('------------------main2------------')
    print(prox)
    list1, name, fan_name, total = get_gif_list(prox, ip_list, length, url)
    is_exist.is_exist_fun(name, fan_name)
    end = time.time()
    print(name)
    print(fan_name)
    print(f'获取{name} {fan_name}所有gif链接耗时', end - start)
    print('list1:')
    print(list1)
    start2 = time.time()
    with ThreadPoolExecutor(10) as t:
        for i in list1:
            print(f'存储的gif_src共{len(list1)}个,应存储{total}个')
            print(f'即将访问 {i} [{list1.index(i)+1}]')
            ind = list1.index(i) + 1
            t.submit(request_reconn_binary.request_reconn_fun, ind, name, fan_name, prox, ip_list, length, i, head, 6, 20)
    end2 = time.time()
    print(f'缓存{name} {fan_name}所有gif到本地耗时', end2 - start2, f'共{total}个gif')


lll = [
    'http://www.boljoo.com/2678.html',
    'http://www.boljoo.com/443.html',
    'http://www.boljoo.com/419.html',
    'http://www.boljoo.com/284.html'
]
for i in lll:
    start = time.time()
    m(i)
    end = time.time()
    print('共耗时', (end - start)/60, 'min')
    winsound.Beep(700, 500)

# m(url)