import os.path

import requests
from lxml import etree
import proxy_pool
import request_reconn
import get_pool
from urllib import parse
import time
import yue
head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
url = 'http://www.boljoo.com/tag/%e4%b8%83%e6%b3%bd%e7%be%8e%e4%ba%9a'


def get_all_fan(url):
    # prox, ip_list, length = get_pool.get_pool_list()
    fout = open('./ip.txt', 'r')
    prox, ip_list, length = yue.ddd(fout)
    fan_url = []
    resp_text = request_reconn.request_reconn_fun(prox, ip_list, length, url, head, 5, 20)
    html = etree.HTML(resp_text)
    lis = html.xpath('//*[@id="post-list"]/ul/li')
    for li in lis:
        href_value = li.xpath('./div/div[1]/a/@href')[0]
        print(href_value)
        fan_url.append(href_value)
    all_fan_sum = len(fan_url)
    return [fan_url, all_fan_sum]


def parse_name(text):
    return parse.unquote(text)


def write_url(url):
    url_list, total = get_all_fan(url)
    encode_name = url.rsplit('/', 1)[1]
    decode_name = parse_name(encode_name)
    if not os.path.exists(f'./test/{decode_name}'):
        os.makedirs(f'./test/{decode_name}')
    fout = open(f'./test/{decode_name}/url.txt', 'a+')
    for i in url_list:
        fout.write(i)
        fout.write('\n')


# url_list, total = get_all_fan(url)
# print(url_list)
# print(total)
s = time.time()
write_url(url)
e = time.time()
print(f'写入url耗时', e - s)