#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name	: process
# Author		: badger
# Created		: 2017/7/18
# Description	: 

from seed import models
from web_crawler import web_content
from django.utils.timezone import utc

import seedmm
import const
import datetime


# todo: multiThread process
def craw(target_url):
    # 删除未处理完成的影片
    for unchecked in models.Movie.objects.filter(check_date=None):
        print unchecked.no + " is unchecked"
        unchecked.delete()
        print "deleted!"

    page = 77
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


def update_by_actors():
    for actor in models.Actors.objects.filter(check_date=None):
        url = actor.actor_url + r'/'
        craw(url)
        actor.check_date = datetime.datetime.now().replace(tzinfo=utc)
        actor.save()
    return const.CRAW_FINISH


def update_uncensored():
    url = r'https://www.seedmm.com/uncensored/page/'
    craw(url)
    return const.CRAW_FINISH


def update_censored():
    url = r'https://www.seedmm.com/page/'
    craw(url)
    return const.CRAW_FINISH
