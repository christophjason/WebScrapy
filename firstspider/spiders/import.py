# -*- coding: utf-8 -*-
import scrapy


class ImportSpider(scrapy.Spider):
    name = 'import'
    allowed_domains = ['scrapy']
    start_urls = ['http://scrapy/']

    def parse(self, response):
        pass
