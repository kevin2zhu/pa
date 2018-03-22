# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

class ShizhanPipeline(object):
    def __init__(self):
        '''打开myjsondata.json文件'''
        self.file =\
        codecs.open('/root/pyfile/py3/myjsondata.json','wb',encoding="utf-8") 

    def process_item(self, item, spider):
        
        #写入数据到json文件中
        i = json.dumps(dict(item),ensure_ascii=False)
        #将数据转为dict,同时关闭ascii编码写入
        line = i +'\n'
        #每条数据后加入换行
        self.file.write(line)
        #写入数据到mydata.json文件中
        return item
    
    def close_json(self,spider):
        
        #关闭json文件
        self.file.close()


