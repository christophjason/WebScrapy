import scrapy

class GojekSpider(scrapy.Spider):
    name = "gojek"

    def start_requests(self):
        urls = [
            'https://gojek.com',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'gojek-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)