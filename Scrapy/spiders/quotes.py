import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.com']
    start_urls = ['http://quotes.com/']

    def parse(self, response):
        pass
