#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name	: web_crawler
# Author		: badger
# Created		: 2017/7/16
# Description	: 

import urllib2

# 强制添加头信息和验证数据，模拟浏览器信息
import time
import const

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'


def web_content(request_url, *data):
    # 生成请求
    login_request = urllib2.Request(request_url, data)
    login_request.add_header('User-Agent', user_agent)
    login_request.add_header('referer', 'https://www.seedmm.com/')

    need_info = True

    # todo: reconnection test
    while need_info:
        try:
            response = urllib2.urlopen(login_request, timeout=8)
            need_info = False
            return response.read()
        except Exception as err:
            if const.HTTP_NOT_FOUND in str(err):
                return const.CRAW_FINISH
            print request_url + "超时，重新连接"
            time.sleep(1)
