# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
url = 'xxx'
postdata = urllib.parse.urlencode({'xxx': 'xxx', 'xxx': 'xxx'}).encode('uft-8')
req = urllib.request.Request(url, postdata)
req.add_header('User-Agent', ' Mozilla/5.0 (Windows NT 10.0; WOW64;\
	 Trident/7.0; rv:11.0) like Gecko') #这个IE的标头
data = urllib.request.urlopen(req).read()

#data中的二进制数据就可以进行保存然后写入到你想要的地方是二进制
