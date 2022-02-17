import requests
from lxml import etree
from bs4 import BeautifulSoup

head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 50 + 1)
]


def spider(url):
    resp = requests.get(url, headers=head)
    return resp.text


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', class_="post-item-title")
    return [(i['href'], i.get_text()) for i in links]


if __name__ == '__main__':
    for i in parse(spider(urls[0])):
        print(i)
