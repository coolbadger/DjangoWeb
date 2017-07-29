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
series_result = models.Series.objects.filter().order_by('-check_date')


def default(request):
    page_no = 1
    page_range = range(1, 6)
    table_result = models.Movie.objects.all()[:30]
    actor_count = models.Actors.objects.count()
    checked_actor_count = result_obj.count()
    movie_count = models.Movie.objects.count()
    magnet_count = models.Magnet.objects.count()
    series_count = series_result.count()
    checked_series_count = series_result.exclude(check_date=None).count()

    total_page = result_obj.count() / 30 - 1

    resp = render_to_response('index.html', locals())
    return resp


def actors(request, page_no):
    if not page_no:
        page_no = 1
    page_no = int(page_no)
    page_count = 30
    actor_count = models.Actors.objects.count()
    checked_actor_count = result_obj.count()
    movie_count = models.Movie.objects.count()
    magnet_count = models.Magnet.objects.count()
    series_count = series_result.count()
    checked_series_count = series_result.exclude(check_date=None).count()

    total_page = result_obj.count() / page_count
    page_range = []
    print total_page

    if page_no < 1:
        return HttpResponseRedirect('/page/1')
    elif page_no >= total_page:
        return HttpResponseRedirect('/page/' + str(total_page - 1))

    for i in range(max(page_no - 2, 1), min(max(page_no - 2, 1) + 5, total_page)):
        page_range.append(i)

    table_result = result_obj.order_by('-check_date')[
                   page_no * page_count - page_count:page_no * page_count]

    resp_data = dict(table.table_date(table_result, page_no, page_range).items() +
                     {'actor_count': actor_count, 'total_page': total_page - 1,
                      'checked_actor_count': checked_actor_count,
                      'movie_count': movie_count,
                      'magnet_count': magnet_count,
                      'series_count': series_count,
                      'checked_series_count': checked_series_count, }.items())
    resp = render_to_response('actors.html', resp_data)
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
        if mm:
            extra_data.append(mm.magnet_url)
            sum_str += mm.magnet_url + '<br/>'

    count = str(ma_results.count()) + " / " + str(len(extra_data))
    resp = render_to_response('seed/actor_resource.html',
                              dict(table.table_date(movies, 1, [1]).items() + {'extra_data': extra_data,
                                                                               'count': count,
                                                                               'sum_str': sum_str}.items()))
    return resp


def series_page(request, page_no):
    if not page_no:
        page_no = 1
    page_no = int(page_no)
    page_count = 30
    series_count = models.Series.objects.count()
    actor_count = models.Actors.objects.count()
    checked_actor_count = result_obj.count()
    movie_count = models.Movie.objects.count()
    magnet_count = models.Magnet.objects.count()
    series_count = series_result.count()
    checked_series_count = series_result.exclude(check_date=None).count()

    for se in series_result:
        if not se.image_url:
            mv = models.Movie.objects.filter(series=se, movie_img_url__contains='.').first()
            if mv:
                se.image_url = mv.movie_img_url

    total_page = series_result.count() / page_count
    page_range = []
    print total_page, page_no

    if page_no < 1:
        return HttpResponseRedirect('/seed/series_page/1')
    elif page_no >= total_page:
        return HttpResponseRedirect('/seed/series_page/' + str(total_page - 1))

    for i in range(max(page_no - 2, 1), min(max(page_no - 2, 1) + 5, total_page)):
        page_range.append(i)

    table_result = series_result.order_by('-check_date')[
                   page_no * page_count - page_count:page_no * page_count]

    resp_data = dict(table.table_date(table_result, page_no, page_range).items() +
                     {'actor_count': actor_count, 'total_page': total_page - 1,
                      'checked_actor_count': checked_actor_count,
                      'movie_count': movie_count,
                      'magnet_count': magnet_count,
                      'series_count': series_count,
                      'checked_series_count': checked_series_count}.items())
    resp = render_to_response('series.html', resp_data)
    return resp


def series_resource(request, serie):
    if not serie:
        return HttpResponseRedirect('/seed/series/')
        serie = int(serie)

    mv_results = models.Movie.objects.filter(series_id=serie)

    # ma_results = models.Movie_Actor.objects.filter(actor_id=serie)
    movies = []
    magnets = []
    extra_data = []
    sum_str = ''
    for mv in mv_results:
        movies.append(mv)
        mm = models.Magnet.objects.filter(movie=mv).first()
        if mm:
            extra_data.append(mm.magnet_url)
            sum_str += mm.magnet_url + '<br/>'

    count = str(mv_results.count()) + " / " + str(len(extra_data))
    resp = render_to_response('seed/series_resource.html',
                              dict(table.table_date(movies, 1, [1]).items() + {'extra_data': extra_data,
                                                                               'count': count,
                                                                               'sum_str': sum_str}.items()))
    return resp
