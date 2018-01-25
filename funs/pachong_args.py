# -*- coding:utf-8 -*-
import urllib.request 


#filename = r'D:\Py\reptile\html_file\1.html'
file = urllib.request.urlopen('https://www.baidu.com')              #将获取的网站的API传给变量file
data = file.read()                                                  #将API中数据提取出来并保存至data中
#urllib.request.urlretrieve('http://www.baidu.com', filename)       #将文件直接保存到目标文件
#urllib.request.urlcleanup()                                        #清楚上条命令的缓存

file.getcode()                                                      #响应状态码 200为响应正确

file.geturl()                                                       #获取url

urllib.request.quote('http://www.sina.com.cn')                      #对url中不符合的字符进行编码
urllib.request.unquote('http%3A//www.sina.com.cn')                  #对编码后的网址进行解码

(模拟浏览器头部）方法一：
headers = ('User-Agent',xxx)                                        #1.头部信息
opener = urllib.request.build_opener()                     			#2.创建自定义的opener,并赋值给opener
opener.addheaders = [headers]                                       #3.设置对应的头部信息(由先前创建)来达到访问不允许爬虫的网站
opener.open(url).read()                                             #4.对应上面的第6行,获取网站API,在urlopen(url,Timeout=s)表示超时

(模拟浏览器头部）方法二：
req = urllib.request.Request(url)                                   #创建一个Request对象赋值给req
req.add_header('User-Agent',xxx)                                    #添加头部信息,类似于上面第3点
filename = urllib.request.urlopen(req).read()                       #对应上面方法一第4点,在urlopen(url,Timeout=s)表示超时

