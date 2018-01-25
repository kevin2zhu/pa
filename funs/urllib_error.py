# -*- coding:utf-8 -*-
import urllib.request
import urllib.error

url = 'xxxx'
try:
	urllib.request.urlopen(url)         #尝试访问该url
except urllib.error.URLError as e:	    #错误处理方式,并将错误重名为e
	if hasattr(e,'code'):
            #hasattr(对象或者方法,要判断的东西是否在这个对象或者方法中)
            print(e.errno)					#处理方式。
	if hasattr(e,'reason'):		
            print(e.reason)
