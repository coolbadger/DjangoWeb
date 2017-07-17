#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name	: web_crawler
# Author		: badger
# Created		: 2017/7/16
# Description	: 

import urllib2

# 强制添加头信息和验证数据，模拟浏览器信息
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'


def web_content(request_url, *data):
    # 生成请求
    login_request = urllib2.Request(request_url, data)
    login_request.add_header('User-Agent', user_agent)
    login_request.add_header('referer', 'https://www.seedmm.com/')

    try:
        response = urllib2.urlopen(login_request, timeout=6)
    except Exception as err:
        print request_url + "超时，重新连接"
        return web_content(request_url, data)

    return response.read()
