# -*- coding: utf-8 -*-
import scrapy


class GrabSpider(scrapy.Spider):
    name = 'grab'

    def start_requests(self):
        urls = [
            'http://hub.grab.com/rides'
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, res):
        page = res.url.split("/")[-2]
        filename = 'grab-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(res.body)
        self.log('Saved File %s' % filename)
