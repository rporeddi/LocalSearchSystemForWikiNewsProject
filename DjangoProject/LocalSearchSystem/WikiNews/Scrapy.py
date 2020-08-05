# -*- coding: utf-8 -*-
"""wikinews_scrapy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D8wuViiZ1zVz6XG0yzkNyFlwBag7269f
"""

import scrapy
import re
import pandas as pd
import unicodedata
from scrapy.crawler import CrawlerProcess
from urllib.parse import urlparse
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


# Varialble Decleration
result = []
all_urls = []
Paragraph_Data = []
continents = []
continents_urls = []


# Spyder class that scraps the wikinews website
class Wikipedia(scrapy.Spider):
    name = "Wikipedia"
    start_urls = [
        "https://en.wikinews.org/wiki/Main_Page"
    ]

    def parse(self, response):
        for sel in response.xpath('//center//big//b'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            continents.append(zip(title, link))
        return continents



class Wikinews(scrapy.Spider):
    name = "Wikinews"

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            result.append((title[0], link[0]))
        return result


class Wikinews_items(scrapy.Spider):
    name = "Wikinews_items"
    allowed_domains = ['en.wikinews.org']

    def parse(self, response):
        parsed_uri = urlparse(response.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

        def _clean(value):
            value = ' '.join(value)
            value = value.replace('\n', '')
            value = unicodedata.normalize("NFKD", value)
            value = re.sub(r' , ', ', ', value)
            value = re.sub(r' \( ', ' (', value)
            value = re.sub(r' \) ', ') ', value)
            value = re.sub(r' \)', ') ', value)
            value = re.sub(r'\[\d.*\]', ' ', value)
            value = re.sub(r' +', ' ', value)
            return value.strip()

        strings = []
        for i in range(0, 100):
            try:
                for node in response.xpath('//*[@id="mw-content-text"]/div/p[{}]'.format(i)):
                    text = _clean(node.xpath('string()').extract())
                    if len(text):
                        strings.append(text)
            except Exception as error:
                strings.append(str(error))

        paragraph_data = {
            'Title': response.css('#firstHeading::text').extract_first(),
            'image': response.xpath(
                '//*[@id="mw-content-text"]//div//table//tbody//tr//td//a//img/@src').extract_first(),
            'strings': strings
        }
        Paragraph_Data.append(paragraph_data)
        return paragraph_data


configure_logging()
runner = CrawlerRunner()


# Crawl function that executes spyders in order
@defer.inlineCallbacks
def crawl():
    yield runner.crawl(Wikipedia)
    for title, link in continents[0]:
        con_cat = 'https://en.wikinews.org/wiki/Category:' + link.replace('/wiki/', '')
        continents_urls.append(con_cat)

    yield runner.crawl(Wikinews, start_urls=continents_urls)
    df = pd.DataFrame(data=result, columns=["title", "link"])
    df.link = 'https://en.wikinews.org' + df.link
    all_urls = list(df.link)

    yield runner.crawl(Wikinews_items, start_urls=all_urls)
    reactor.stop()


crawl()
reactor.run()  # the script will block here until the last crawl call is finished

Paragraph_Data
