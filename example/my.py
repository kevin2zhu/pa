# -*- coding: utf-8 -*-
import scrapy
from zhizhu.items import ZhizhuItem

class MySpider(scrapy.Spider):
    name = 'my'
    #allowed_domains = ['jd.com']
    start_urls = ('http://jd.com/')
    
    #新增属性urls
#    urls = ('http://www.jd.com',
#            'http://www.qq.com',
#            'http://yum.iqianyue.com'
#           )
    #重写start_requests()方法
#    def start_requests(self):
#        #设置起始网址从新属性urls获取
#        for url in self.urls:
#            yield self.make_requests_from_url(url)
    def __init__(self,myurl=None,*args,**kwargs):
        super(MySpider,self).__init__(*args,**kwargs)
#        MySpider.__init__(self,*args,**kwargs)
        myurllist = myurl.split('|')
        for i in myurllist:
            print('要爬取的网址为:%s'%i)
        self.start_urls = myurllist

    def parse(self, response):
        item = ZhizhuItem()
        item['urlname'] = response.xpath('/html/head/title/text()')
        print('以下将显示爬取的网址的标题:')
        print(item['urlname'])
