# -*- coding: utf-8 -*-
import scrapy
from shizhan.items import ShizhanItem
from scrapy.http import Request

class AutopjtSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = ('http://category.dangdang.com/pg1-cid4003761.html',)
    
    def parse(self, response):
        item = ShizhanItem()
        #通过各种XPATH表达式分别提取商品的名称、价格、链接、评论等信息
        item['name'] = response.xpath('//a[@class="pic"]/@title').extract()
       #获取a标签中的class属性为pic的title属性的值
        item['price'] =\
        response.xpath("//span[@class='price_n']/text()").extract()
       #获取span标签中的class属性为price_n的text值
        item['link'] = response.xpath('//a[@class="pic"]/@href').extract()
       #获取a标签中的class属性为pic的href属性的值
        item['comnum'] = response.xpath('//a[@ddclick]/text()').extract()
       #获取a标签中的name属性为p_pl的text值
      #提取完返回item
        yield item

      #循环爬取xx数据
        for i in range(1,6):
          #通过上面的总结构造要爬取的网址
            url = "http://category.dangdang.com/pg"+str(i)+"-cid4003761.html"
          #通过yield返回Request,并指定要爬取的网址和回调函数
            yield Request(url,callback=self.parse)
          #实现自动爬取
