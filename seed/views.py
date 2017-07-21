# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from seed import models
from seed.crawler import process
from django.http import HttpResponseRedirect
import threading
from component import table

# Create your views here.

task = threading.Thread(target=process.update_all)

result_obj = models.Actors.objects.filter(image_url__contains='.jpg').exclude(check_date=None)


def default(request):
    page_no = 1
    page_range = range(1, 6)
    table_result = result_obj[:30]
    actor_count = models.Actors.objects.count()
    checked_actor_count = result_obj.count()
    movie_count = models.Movie.objects.count()
    magnet_count = models.Magnet.objects.count()

    total_page = result_obj.count() / 30 - 1

    resp = render_to_response('index.html', locals())
    return resp


def page(request, page_no):
    if not page_no:
        page_no = 1
    page_no = int(page_no)
    page_count = 30
    actor_count = models.Actors.objects.count()
    checked_actor_count = result_obj.count()
    movie_count = models.Movie.objects.count()
    magnet_count = models.Magnet.objects.count()

    total_page = result_obj.count() / page_count
    page_range = []
    print total_page

    if page_no <= 1:
        return HttpResponseRedirect('/')
    elif page_no >= total_page:
        return HttpResponseRedirect('/page/' + str(total_page - 1))

    for i in range(max(page_no - 2, 1), min(max(page_no - 2, 1) + 5, total_page)):
        page_range.append(i)

    table_result = result_obj[
                   page_no * page_count - page_count:page_no * page_count]

    resp_data = dict(table.table_date(table_result, page_no, page_range).items() +
                     {'actor_count': actor_count, 'total_page': total_page - 1,
                      'checked_actor_count': checked_actor_count,
                      'movie_count': movie_count,
                      'magnet_count': magnet_count}.items())
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


def actor_resource(request, actor):
    if not actor:
        return HttpResponseRedirect('/')
        actor = int(actor)

    ma_results = models.Movie_Actor.objects.filter(actor_id=actor)
    movies = []
    magnets = []
    extra_data = []
    sum_str = ''
    for ma in ma_results:
        movies.append(ma.movie)
        mm = models.Magnet.objects.filter(movie=ma.movie).first()
        extra_data.append(mm.magnet_url)
        sum_str += mm.magnet_url + '<br/>'

    count = str(ma_results.count()) + " / " + str(len(extra_data))
    resp = render_to_response('seed/actor_resource.html',
                              dict(table.table_date(movies, 1, [1]).items() + {'extra_data': extra_data,
                                                                               'count': count,
                                                                               'sum_str': sum_str}.items()))
    return resp
