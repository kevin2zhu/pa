#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import urllib.request

def getcontent(url,page):
    '''爬取的页面的函数'''
    headers = ('User-Agent','')
