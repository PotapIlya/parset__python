
import asyncio

import urllib3
from urllib.request import Request, urlopen  # Python 3
from bs4 import BeautifulSoup
import certifi
import urllib
import requests
import urllib


def request(url):
    try:
        resp = urlopen(Request(url))
        if resp.getcode() != 200:
            print("Ошибка, Код ответа: %s", resp.getcode())
            return

        # Если дошли до сюда, значит ошибок не было
        return resp.read()
    except ConnectionError:
        http = urllib3.PoolManager(ca_certs=certifi.where())
        resp = http.request('GET', url)
        if resp.status != 200:
            print("Ошибка, Код ответа: %s", resp.status)
            return

        # Если дошли до сюда, значит ошибок не было
        return resp


def download(url, index):
    img = urllib.request.urlopen(url).read()
    out = open( index+".jpg", "wb")
    out.write(img)
    out.close


url = 'http://ibmg.ru/label'
index = 0
html = BeautifulSoup(request(url), 'html5lib')

wrapper = html.find("div", class_='musicians-slider')

items = wrapper.find_all("img")

for item in items:
    index += 1
    download( item['src'], str(index) )





print('end...')

