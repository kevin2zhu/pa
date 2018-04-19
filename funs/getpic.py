#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import urllib.request
import re
import urllib.error

html_add = 'xxxx'                                   #获取需要爬虫的网址
url = urllib.request.urlopen(html_add).read()       #取得url的byte形式
url = str(url)
pat = '(http://.+?.jpg|png)'                        #正则分析想要取得的图片链接
data = re.compile(pat).findall(url)                 #将正则匹配到结果赋值给data,此时data是个list

#urlretrieve是一个将结果存储下来的方法具体使用看下面,增加一个判断链接失效就跳过
for i in data:
    try:
        urllib.request.urlretrieve(imageurl,'ospath\' + finename='xxx')
        excepet urllib.error.URLError as e:
            if hasattr(e,'code'):
                print(e,'code')
            if hasattr(e,'reason'):
                print(e,'reason')




