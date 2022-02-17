import requests
from lxml import etree
import re
from bs4 import BeautifulSoup

head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
url = 'http://www.boljoo.com/4460.html/1'


resp = requests.get(url, headers=head)
# html = etree.HTML(resp.text)
# content = html.xpath('/html/body/div[1]/div[2]/div[1]/div/article/div[1]/p[2]/br')
# for i in content:
#     print(i.)
# soup = BeautifulSoup(resp.text, 'html.parser')
# br = soup.find_all()
page = resp.text
obj = re.compile(r'/><br />(?P<cont>.*?)</p>', re.S)
br = re.findall(obj, page)
cont = br.pop()
no_blank = cont.replace(' ', '')
print(no_blank)
name = no_blank.split('：')[1][:-3]
fan_name = no_blank.split('：')[2]
print(name)
print(fan_name)
