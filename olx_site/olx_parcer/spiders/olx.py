import scrapy
from urllib.parse import urljoin, urlparse
from olx_parcer.items import OlxParcerItem
import unicodedata


class OlxSpider(scrapy.Spider):
    name = "olx"
    start_urls = [
        'https://www.olx.ua/rabota/cekretariat-aho/',
    ]

    visited_urls = []

    def parse(self, response):
        if response.url not in self.visited_urls:
            self.visited_urls.append(response.url)
            for obj_link in response.xpath('//a[contains(@class, "detailsLink")]/@href').extract():
                url = urljoin(response.url, obj_link)
                print(url)
                yield response.follow(url, callback=self.parse_obj)

            next_page = response.xpath('//a[contains(@data-cy, "page-link-next")]/@href').extract()

            if len(next_page) > 0:
                next_page_url = urljoin(response.url + '/', next_page[-1])

                yield response.follow(next_page_url, callback=self.parse)

    def remove_control_characters(s):
        return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")

    def parse_obj(self, response):
        item = OlxParcerItem()
        date = response.xpath('//span[contains(@class, "pdingleft10 brlefte5")]').extract()
        item['date'] = date
        yield item
