import asyncio

import urllib3
from urllib.request import Request, urlopen  # Python 3
from bs4 import BeautifulSoup
import certifi

from Db import create_sql
from Db import check_sql

import re
import config


class Parser:

    index = 1
    url = ''
    type = ''
    wrapper = ''
    item = ''
    title = ''
    price = ''
    text = ''

    def __init__(self, data):

        self.type = data['type']
        self.url = data['url']
        self.wrapper = data['wrapper']
        self.item = data['item'],
        self.title = data['title'],
        self.price = data['price'],
        self.text = data['text'],

        self.page()

    def page(self):
        print(str(self.index) + ' page')

        html = BeautifulSoup(self.request(self.url + str(self.index)), 'html5lib')
        wrapper = html.find("table", class_=self.wrapper)

        if wrapper:
            items = wrapper.find_all("div", class_=self.item)
            if items:
                page_parse = self.parse_page(items)
                if page_parse:
                    self.index += 1
                    self.page()
            else:
                print('Error not item')
        else:
            print('Error not wrapper')

    def sql(self, sql):
        return asyncio.get_event_loop().run_until_complete(sql)

    def parse_page(self, items):
        for item in items:
            type_id = self.type + item['data-id']
            check = self.sql(check_sql(type_id))

            print(check)

            if check:
                title = item.find("div", class_=self.title).find('a', href=True).text
                print(title)
                price = item.find("div", class_=self.price).text

                pr = ''
                for e in re.findall(r'\d+', price):
                    pr += e

                href = item.find("div", class_=self.title).find('a', href=True)['href']
                text = BeautifulSoup(self.request(href), 'html5lib').find("div",
                                                                          class_=self.text).text
                self.sql(create_sql(title, pr, href, text, type_id))

        return True

    def request(self, url):
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


Parser(config.freelancehunt)
