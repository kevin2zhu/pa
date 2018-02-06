# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from csvpj.items import CsvpjItem

class MycsvspriderSpider(CSVFeedSpider):
    name = 'mycsvsprider'
    allowed_domains = ['iqianyue.com']
    #定义要处理的csv文件所在的网址
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/mydata.csv']
    
    #定义headers
    headers = ['name', 'sex', 'addr', 'email']
    #定义分隔符
    delimiter = ','

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = CsvpjItem()
        #提取各行的同属性这一列的信息如,name、sex
        i['name'] = row['name'].encode()
        i['sex'] = row['sex'].encode()
        #i['url'] = row['url']
        #i['name'] = row['name']
        #i['description'] = row['description']
        
        #进行信息输出
        print('名字是:%s'%i['name'])
        print('性别是:%s'%i['sex'])
        print('----------------->')
        return i
