# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

class NbaPipeline(object):

    def __init__(self):
        '''创建存放数据的文件'''
        
        self.file =\
        codecs.open('/root/data/nba_news.json','wb',encoding="utf-8")
    
    def process_item(self, item, spider):
        '''写入数据到json文件'''
        
        i = json.dumps(dict(item),ensure_ascii=False)
        #将数据转为dict,同时关闭ascii编码写入到json文件中
        line = i +'\n'
        #每写一条换一行
        self.file.write(line)
        return item
    
    def close_file(selfi,spider):
        '''关闭文件'''
        
        self.file.close()
