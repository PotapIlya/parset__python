from bs4 import BeautifulSoup
import urllib3
import certifi
import asyncio
from potap.migr.catalogs.add import add_category
from potap.migr.items.add import add_item
from urllib.request import Request, urlopen  # Python 3
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO)
log = logging.getLogger("ex")


def start_sql(sql):
    asyncio.get_event_loop().run_until_complete(sql)


def request(url):
    try:
        req = Request(url)
        resp = urlopen(req)
        if resp.getcode() != 200:
            log.info("Ошибка, Код ответа: %s", resp.getcode())
            return

            # Если дошли до сюда, значит ошибок не было
        return resp.read()
    except ConnectionError:
        http = urllib3.PoolManager(ca_certs=certifi.where())
        resp = http.request('GET', url)
        if resp.status_code != 200:
            log.info("Ошибка, Код ответа: %s", resp.status)
            return

        # Если дошли до сюда, значит ошибок не было
        return resp


class Parser:
    i = 0
    url_s = 'https://erolaif.ru'
    catalog = '/shop'

    def __init__(self):
        self.catalog_f(self.url_s + self.catalog)

    def items_p(self, items_page_url, j):
        items = request(self.url_s + items_page_url)
        soup_i = BeautifulSoup(items, 'html5lib')
        items_page = soup_i.find("div", attrs={"class": "shop-items-list"})
        if items_page:
            items_list = items_page.find("div", attrs={"class": "js_shop_items_list"})
            for item in items_list.find_all("div", attrs={"class": "shop-item"}):
                start_sql(add_item(self.i, item.a.attrs["href"],
                                   item.find("span", attrs={"class": "shop-item__caption"}).text,
                                   item.find("div", attrs={"class": "shop-item__price"}).span.text))
                j += 1

            pagination = items_page.find("ul", attrs={"class": "pagination"})
            if pagination:
                next_p = pagination.find("li", attrs={"class": "next"})
                if next_p:
                    self.items_p(next_p.a.attrs['href'], j)
        else:
            self.catalog_f(self.url_s + items_page_url)

    def catalog_f(self, url):
        self.i += 1
        page = request(url)
        soup = BeautifulSoup(page, 'html5lib')

        # print(soup.prettify())
        catalog_list = soup.find("div", attrs={"class": "catalog-list"})

        for tag in catalog_list.find_all("a"):
            start_sql(add_category(1, tag.attrs["href"], tag.attrs["title"], self.i))
            self.items_p(tag.attrs["href"], 0)
            self.i += 1


Parser()
