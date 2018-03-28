# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class UsedbPipeline(object):
    def __init__(self):
        #程序初始化并建立数据库的连接
        self.conn =\
        pymysql.connect(host='127.0.0.1',user='root',passwd='10086130',db='mypy3db',charset="utf8")
        self.cur = self.conn.cursor()
    
    def process_item(self, item, spider):
        #将获取的name和keywd分别赋给变量name和key
        name = item['name'][0]
        context = item['context'][0]
        #构造对应的Sql语句
        sql = 'insert into mytb(hero_name,context)VALUES("%s","%s")'%(name,context)

       # 通过query实现执行对应的Sql语句
        self.cur.execute(sql)
        self.conn.commit()
        return item

    def close_db(self,spider):
        self.conn.close()
