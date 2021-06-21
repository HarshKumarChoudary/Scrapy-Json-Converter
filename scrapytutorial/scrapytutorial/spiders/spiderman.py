import scrapy
from ..items import ScrapytutorialItem

class SpidermanSpider(scrapy.Spider):
    name = 'spiderman'
    start_urls = ['https://wisdomquotes.com/short-quotes']

    def parse(self, response):
        items = ScrapytutorialItem()
        Quotes_all = response.xpath('//blockquote')

		# These paths are based on the selectors
		
        for quote in Quotes_all:
            items['Quote'] = quote.css('p::text').extract()
            yield items
