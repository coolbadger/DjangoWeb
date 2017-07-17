# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
import threading

from seed.crawler.web_crawler import web_content
from seed.crawler import seedmm


# Create your views here.


def craw(target_url, name):
    page = 1
    while (True):
        uncensored = 'n'
        validate_url = target_url + str(page)
        if 'uncensored' in validate_url:
            uncensored = 'y'
        print "start seeking at: " + validate_url
        result_context = web_content(validate_url)
        msg = seedmm.movie_expression(result_context, uncensored)
        print "page " + str(page) + " complite"

        for property, value in vars(msg).iteritems():
            print property, ": ", value

        page += 1
    return name + "end"


def default(request):
    threads = []
    censored = threading.Thread(target=craw, args=(r'https://www.seedmm.com/page/', 'censored'))

    threads.append(censored)

    for thread in threads:
        thread.setDaemon(True)
        thread.start()

    resp = render_to_response('index.html', locals())
    return resp
