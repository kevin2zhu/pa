# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from nba.items import NbaItem

class InfoSpider(CrawlSpider):
    name = 'info'
    allowed_domains = ['nba.hupu.com']
    start_urls = ['http://nba.hupu.com/']

    rules = (
        Rule(LinkExtractor(allow=('.html'),allow_domains=('nba.hupu.com')),callback='parse_item',
             follow=False),
    )

    def parse_item(self, response):
        i = NbaItem()
        i['name'] = response.xpath('//ul/li/a/text()').extract()
        i['link'] = response.xpath('//ul/li/a[@target="_blank"]/@href').extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
