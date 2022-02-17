import requests
import request_reconn
from lxml import etree
import re
head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}


def get_btn_amount(prox, ip_list, length, url):
    resp_text = request_reconn.request_reconn_fun(prox, ip_list, length, url, head, 6, 20)
    html = etree.HTML(resp_text)
    a_s = html.xpath('//*[@id="primary-home"]/article/div[1]/div/a')
    total = len(a_s) + 1
    # get name
    page = resp_text
    # print(page)
    # obj = re.compile(r'/><br />(?P<cont>.*?)</p>', re.S)
    # br = re.findall(obj, page)
    # for i in br:
    #     print(i)
    # cont = br.pop()
    # no_blank = cont.replace(' ', '')
    # print(no_blank)
    # name = no_blank.split('：')[1][:-3]
    # fan_name = no_blank.split('：')[2]
    ################
    cont = html.xpath('/html/head/meta[16]/@content')[0]
    print(cont)
    con = cont.split(',')
    fan_name = con[0]
    name = con[1]
    print(cont)
    print(name)
    print(fan_name)
    ###################
    return [total, name, fan_name]


# get_btn_amount('http://www.boljoo.com/4107.html')
#//*[@id="primary-home"]/article/div[1]/p[2]/img
#//*[@id="primary-home"]/article/div[1]/p[2]/img