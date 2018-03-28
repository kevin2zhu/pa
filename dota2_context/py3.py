# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from usedb.items import UsedbItem

class Py3Spider(CrawlSpider):
    name = 'py3'
    allowed_domains = ['dota2.com.cn']
    start_urls = ['http://www.dota2.com.cn/heroes/']

    rules = (
        Rule(LinkExtractor(allow=('http://www.dota2.com.cn/hero/.*?/')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = UsedbItem()
        hero = {}
        i['name'] = response.xpath('//img[@class="hero_b"]/@alt').extract()
        text = response.xpath('//div[@class="story_box h120"]/text()').extract()
        newtext = "".join(text)
        beijing = newtext.strip()
        hero['beijing'] = beijing
        context = list(hero.values())
        i['context'] = context
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
