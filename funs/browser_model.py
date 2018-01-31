# -*- coding:utf-8 -*-
import urllib.request
import http.cookiejar

# 构建地址栏和头部信息
url = 'xxx'
headers = {'Accept': ' text/html,application/xhtml+xml,application/xml;q=039,*/*;q=0.8',
           'Accept-Encoding': 'gb2312,uft-8',
           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
           'Connection': 'keep-alive', 'referer': 'baidu.com'}

# 创建头部和代理或者cookie
proxy = urllib.request.ProxyHandler({'http': 'ipaddr'})           #代理
cjar = http.cookiejar.CookieJar()								  #Cookie

#创建opener
opener = urllib.request.build_opener( 
    proxy, urllib.request.HTTPHandler,urllib.request.HTTPCookieProcessor(cjar))
headall = []
for k,v in headers.items():
	items = (k,v)
	headall.append(items)
#将浏览器信息添加到opener中去
opener.addheaders = headall

#安装opener到全局
urllib.request.intsall_opener(opener)

data = urllib.request.urlopen(url).read()
