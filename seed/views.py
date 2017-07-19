# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from seed import models
from seed.crawler import process
import threading

# Create your views here.

task = threading.Thread(target=process.update_all)


def default(request):
    resp = render_to_response('index.html')
    return resp


def process_start(request):
    print 'start'
    if not task.isAlive():
        task.setDaemon(True)
        task.start()
    resp = render_to_response('craw.html')
    return resp


def process_stop(request):
    if task.isAlive():
        task.join()
    resp = render_to_response('index.html')
    return resp
