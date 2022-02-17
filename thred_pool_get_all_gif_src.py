import queue
import time
from concurrent.futures import ThreadPoolExecutor
import request_reconn
from lxml import etree
import get_btn

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

url = 'http://www.boljoo.com/2602.html'


def parse(resp_text):
    html = etree.HTML(resp_text)
    src_value = html.xpath('//*[@id="primary-home"]/article/div[1]/p[2]/img/@src')[0]
    print(src_value)
    return src_value


def get_gif_src(prox, ip_list, length, url, diji, share_q: queue.Queue):
    resp_text = request_reconn.request_reconn_fun(prox, ip_list, length, url + f'/{diji}', head, 6, 30)
    # time.sleep(2)
    src_value = parse(resp_text)
    share_q.put(src_value)


def get_gif_list(prox, ip_list, length, url):
    temp_list = []
    q = queue.Queue()
    toatal, name, fan_name = get_btn.get_btn_amount(prox, ip_list, length,  url)
    with ThreadPoolExecutor() as t:
        for i in range(1, toatal + 1):
            t.submit(get_gif_src, prox, ip_list, length, url, i, q, )
    for i in range(0, q.qsize()):
        temp_list.append(q.get())
    return [temp_list, name, fan_name, toatal]


# result = get_gif_list(url)
# for i in range(1, result.qsize()):
#     print(result.get())
