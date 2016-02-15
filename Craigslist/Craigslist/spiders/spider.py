import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from Craigslist.items import CraigslistItem


class MySpider(CrawlSpider):
    name = 'craigslist'
    allowed_domains = ["sanantonio.craigslist.org"]
    start_urls = ["http://sanantonio.craigslist.org/search/jjj"]

    rules = (
            Rule(LinkExtractor(allow = (), restrict_xpaths = ('//a[@class="button next"]',)), callback = "parse_items", follow = True),
                )

    def parse_items(self, response):
        items = []
        for elem in response.xpath('//span[@class="pl"]'):
            item = CraigslistItem() 
            item['title'] = elem.xpath("a/text()").extract()
            item['link'] = elem.xpath("a/@href").extract()
            items.append(item)
        return items

            

