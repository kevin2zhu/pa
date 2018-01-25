# -*- coding:utf-8 -*-
import urllib.request

url = 'xxxxx'
httpd = urllib.request.HTTPHandler(debuglevel=1)
httpshd = urllib.request.HTTPSHandler(debuglevel=1)
opener = urllib.request.build_opener(httpd,httpshd)
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url)                    

#此时的data是一个http对象空间,如需写入需要加以下:
new_data = data.read()
#或者如下:
data = urllib.request.urlopen(url).read()
#此时既可以写入文件中，也会打印出日志出来

