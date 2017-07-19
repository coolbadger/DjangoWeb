# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from seed import models
from seed.crawler import process
from django.http import HttpResponseRedirect
import threading

# Create your views here.

task = threading.Thread(target=process.update_all)


def default(request):
    page_no = 1
    page_range = range(1, 6)
    table_result = models.Actors.objects.exclude(image_url="")[:30]

    resp = render_to_response('index.html', locals())
    return resp


def page(request, page_no):
    if not page_no:
        page_no = 1
    page_no = int(page_no)
    page_count = 30
    total_page = models.Actors.objects.count() / page_count
    page_range = []
    print total_page

    if page_no <= 1:
        return HttpResponseRedirect('/')
    elif page_no >= total_page:
        return HttpResponseRedirect('/page/' + str(total_page))

    for i in range(max(page_no - 2, 1), max(page_no - 2, 1) + 5):
        page_range.append(i)

    table_result = models.Actors.objects.order_by('cup')[
                   page_no * page_count - page_count:page_no * page_count]

    resp_data = {'table_result': table_result, 'page_no': page_no, 'page_range': page_range}
    resp = render_to_response('index.html', resp_data)
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
