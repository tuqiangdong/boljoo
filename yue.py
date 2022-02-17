import requests

head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
url = 'http://webapi.http.zhimacangku.com/getip?num=20&type=1&pro=0&city=0&yys=0&port=1&pack=215161&ts=0&ys=0&cs=0&lb=4&sb=0&pb=4&mr=1&regions='


def get_ip_txt(url):
    resp = requests.get(url, headers=head)
    with open('./ip.txt', 'w') as f:
        f.write(resp.text)


def ddd(fout):
    ip_list = []
    prox = []
    text = fout.readlines()
    for i in text:
        temp = i.strip('\n')
        ip_list.append(temp)
    for i in ip_list:
        dic = {"http": f"{i}", "https": f"{i}"}
        prox.append(dic)
    length = len(prox)
    print(ip_list)
    return [prox, ip_list, length]


# get_ip_txt(url)
#     fout = open('./ip.txt', 'r')
#     ddd(fout)
