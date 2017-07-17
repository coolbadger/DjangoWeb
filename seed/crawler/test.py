#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name	: test
# Author		: badger
# Created		: 2017/7/16
# Description	:
import math
import random

import datetime

from django.utils.timezone import utc

import util

import web_crawler

# floor = int(math.floor(random.random() *1e3 + 1))
#
full_str = r'<span class="genre"><a href="https://www.seedmm.com/genre/3u">特典あり（AVベースボール）</a></span>'
str= r'<span class="genre"><a href="(https://www.seedmm.com/.*?)">(.{1,64}?)</a></span>'

print util.findall(str,full_str)

# url =r'https://www.seedmm.com/ajax/uncledatoolsbyajax.php?gid=6747707738&lang=zh&img=https://images.javbus.info/cover/10jr_b.jpg&uc=1&floor='+str(floor)
# print url
# print web_crawler.web_content(url)

# print datetime.datetime.now().replace(tzinfo=utc)