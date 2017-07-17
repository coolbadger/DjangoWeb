#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name	: main
# Author		: badger
# Created		: 2017/7/17
# Description	: 

import seedmm
import const
from web_crawler import web_content


def craw(target_url):
    page = 1
    while (True):
        uncensored = 'n'
        validate_url = target_url + str(page)
        if 'uncensored' in validate_url:
            uncensored = 'y'
        print "start seeking at: " + validate_url
        result_context = web_content(validate_url)
        if result_context == const.CRAW_FINISH:
            msg = validate_url + " is the end"
            print msg
            return msg
        msg = seedmm.movie_expression(result_context, uncensored)
        print "page " + str(page) + " complite"

        for property, value in vars(msg).iteritems():
            print property, ": ", value

        page += 1
