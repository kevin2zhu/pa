# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse


def user_proxy(proxy_addr, url):
    import urllib.request
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})               #代理对象
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler) #自定义opener对象 
    urllib.request.install_opener(opener)                                   #全局使用该对象
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data

