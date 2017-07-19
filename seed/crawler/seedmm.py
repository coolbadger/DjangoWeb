#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# coding=utf8

# Script Name	: seedmm
# Author		: badger
# Created		: 2017/7/15
# Description	:
import math
import random

import datetime
import threading

from django.utils.timezone import utc

from seed import models
from web_crawler import web_content
from util import search_str, findall, fix_esc_str


class Result_Msg(object):
    actor_count = 0
    procced_count = 0
    total_count = 0
    movie_count = 0
    resource_count = 0
    tag_count = 0
    uncensored = r'n'

    def reset(self):
        self.actor_count = 0
        self.procced_count = 0
        self.movie_count = 0
        self.resource_count = 0
        self.tag_count = 0

    pass


result_msg = Result_Msg()


def movie_expression(context, censored_info):
    result_msg.uncensored = censored_info
    result_msg.reset()

    movies_url_tr = r'<a class="movie-box" href="(.*?)">'  # web_context = url

    movie_results = findall(movies_url_tr, context)
    result_msg.total_count = len(movie_results)
    tasks = []
    for line in movie_results:
        process_task(line,context)
    #     new_task = threading.Thread(target=process_task, args=(line, context,))
    #     tasks.append(new_task)
    #
    # for task_item in tasks:
    #     if not task_item.isAlive():
    #         task_item.setDaemon(True)
    #         task_item.start()
    # while result_msg.procced_count == result_msg.total_count:
    #     return result_msg
        # process_task(line, context)
        # procced_count += 1
        # print "Processing: " + str(procced_count) + "/" + str(result_msg.total_count) + " \t" + " saved: " \
        #       + str(result_msg.movie_count) + " uncensored: " + result_msg.uncensored
        # new_movie = detail_expression(line)
        # if new_movie.movie_img_url == None:
        #     movie_img_url = r'<a class="movie-box" href="' + line \
        #                     + '">[\s|\S]{70,80}<img src="(https://.{4,64}/thumb\w{0,1}/[\w|\.]{1,16})"'
        #     new_movie.movie_img_url = search_str(movie_img_url, context)
        #     new_movie.save()
        #     print new_movie.movie_img_url + " preview image saved."
        # print str(procced_count) + "/" + str(result_msg.total_count) + " end\n"
    return result_msg


def process_task(movie_url, movie_context):
    result_msg.procced_count += 1
    print "Processing: " + str(result_msg.procced_count) + "/" + str(result_msg.total_count) + " \t" + " saved: " \
          + str(result_msg.movie_count) + " uncensored: " + result_msg.uncensored
    new_movie = detail_expression(movie_url)
    if new_movie.movie_img_url == None:
        movie_img_url = r'<a class="movie-box" href="' + movie_url \
                        + '">[\s|\S]{70,80}<img src="(https://.{4,64}/thumb\w{0,1}/[\w|\.]{1,16})"'
        new_movie.movie_img_url = search_str(movie_img_url, movie_context)
        new_movie.save()
        print new_movie.movie_img_url + " preview image saved."
    print str(result_msg.procced_count) + "/" + str(result_msg.total_count) + " end\n"


def detail_expression(detail_url):
    new_movies = models.Movie.objects.filter(movie_url=detail_url)
    print detail_url

    if new_movies:
        return new_movies.first()
    new_movie = models.Movie(movie_url=detail_url)

    detail_context = web_content(detail_url)

    title_str = r'<h3>(.*?)</h3>'
    no_str = r'<p><span class="header">識別碼:</span> <span style="color:#CC0000;">(.*?)</span></p>'
    date_str = r'<p><span class="header">發行日期:</span> (.*?)</p>'
    length_str = r'<p><span class="header">長度:</span> (.*?)</p>'
    director_str = r'<p><span class="header">導演:</span> <a href="https://www.seedmm.com/director/\w{1,64}">(.*?)</a></p>'
    maker_str = r'<p><span class="header">製作商:</span> <a href="https://www.seedmm.com/studio/\w{1,64}">(.*?)</a></p>'
    series_str = r'<p><span class="header">系列:</span> <a href="(https://www.seedmm.com/series/\w{1,64}?)">(.*?)</a></p>'
    tag_str = r'<span class="genre"><a href="(https://www.seedmm.com/.*?)">(.{1,64}?)</a></span>'
    if result_msg.uncensored == 'y':
        actors_url_str = r'<a href="(https://www.seedmm.com/uncensored/star/\w{1,16})">(.{1,64}?)</a>'
    else:
        actors_url_str = r'<a href="(https://www.seedmm.com/star/\w{1,16})">(.{1,64}?)</a>'

    gid_str = r'var gid = (.*?);'
    uc_str = r'var uc = (.*?);'
    img_str = r'var img = \'(.*?)\';'

    new_movie.title = search_str(title_str, detail_context)
    new_movie.no = search_str(no_str, detail_context)
    new_movie.date = search_str(date_str, detail_context)
    new_movie.length = search_str(length_str, detail_context)
    new_movie.director = search_str(director_str, detail_context)
    new_movie.maker = search_str(maker_str, detail_context)

    new_movie.gid = search_str(gid_str, detail_context)
    new_movie.uc = search_str(uc_str, detail_context)
    new_movie.img = search_str(img_str, detail_context)
    new_movie.uncensored = result_msg.uncensored

    series_results = findall(series_str, detail_context)
    for series_info in series_results:
        series_list = models.Series.objects.filter(series_url=series_info[0], name=series_info[1])
        if not series_list:
            series = models.Series(series_url=series_info[0], name=series_info[1])
            series.save()
            print "Series " + series.name + " saved"
        else:
            series = series_list.first()
        new_movie.series = series

    new_movie.save()

    message = "Movie: " + new_movie.no + " saved!"
    print message
    result_msg.movie_count += 1

    # 根据Movie信息更新magnet表
    get_magnets(new_movie)

    actors_results = findall(actors_url_str, detail_context)
    for line in actors_results:
        new_actor = actor_expression(line[0], line[1])
        models.Movie_Actor(movie=new_movie, actor=new_actor).save()

    tag_results = findall(tag_str, detail_context)
    for line in tag_results:
        new_tag = tag_expression(line[0], line[1])
        models.Movie_Tag(movie=new_movie, tag=new_tag).save()
        new_movie.check_done = 'y'
        new_movie.save()

    # for property, value in vars(movie).iteritems():
    #     print property, ": ", value

    new_movie.check_date = datetime.datetime.now().replace(tzinfo=utc)
    new_movie.save()

    return new_movie


def actor_expression(actor_url, name):
    actor = models.Actors.objects.filter(actor_url=actor_url, name=name)
    if actor:
        return actor.first()

    actor = models.Actors(actor_url=actor_url, name=name)
    actor_context = web_content(actor_url)

    start_str = r'<p>'
    end_str = r': (.*?)</p>'
    image_url_str = r'<img src="(https://.{4,64}/actress/.{1,16})" title="' + fix_esc_str(name) + '">'

    actor.cup = search_str(start_str + r'罩杯' + end_str, actor_context)
    actor.age = search_str(start_str + r'年齡' + end_str, actor_context)
    actor.birth = search_str(start_str + r'生日' + end_str, actor_context)
    actor.heigth = search_str(start_str + r'身高' + end_str, actor_context)
    actor.bust = search_str(start_str + r'胸圍' + end_str, actor_context)
    actor.waist = search_str(start_str + r'腰圍' + end_str, actor_context)
    actor.hips = search_str(start_str + r'臀圍' + end_str, actor_context)
    actor.hometown = search_str(start_str + r'出生地' + end_str, actor_context)
    actor.hobby = search_str(start_str + r'愛好' + end_str, actor_context)
    actor.uncensored = result_msg.uncensored
    actor.image_url = search_str(image_url_str, actor_context)

    actor.save()
    print "Actor :" + actor.name + " saved!"
    result_msg.actor_count += 1

    return actor


def tag_expression(tag_url, tag_name):
    tags = models.Tag.objects.filter(tag_url=tag_url, name=tag_name)
    if tags:
        return tags.first()
    tag = models.Tag(tag_url=tag_url, name=tag_name)
    try:
        tag.save()
    except:
        print "Tag saved faile! tag_url: " + tag_url
    result_msg.tag_count += 1
    return tag


def get_magnets(movie_info):
    # url中有网络接口添加的相关认证
    floor = int(math.floor(random.random() * 1e3 + 1))
    magnet_list_url = r'https://www.seedmm.com/ajax/uncledatoolsbyajax.php?gid=' + movie_info.gid + '&lang=zh&img=' + movie_info.img + '&uc=' + movie_info.uc + '&floor=' + str(
        floor)
    magnet_context = web_content(magnet_list_url)

    magnet_str = r'<tr.*>\s*<td.*>\s*<a.*(magnet.*?)">\s*(.*?)\s*</a>\s*</td>\s*<td.*>\s*<a.*">\s*(.*?)\s*</a>\s*</td>\s*<td.*>\s*<a.*">\s*(.*?)\s*</a>\s*</td>\s*</tr>'
    magnet_result = findall(magnet_str, magnet_context)
    magnet_count = 0
    for line in magnet_result:
        magnets = models.Magnet(title=movie_info.title, movie=movie_info, magnet_url=line[0])

        if len(search_str(r'(.*?)<a\s', line[1])) > 1:
            magnets.file_name = search_str(r'(.*?)<a\s', line[1])
            magnets.hd = 'y'
        else:
            magnets.file_name = line[1]
        magnets.size = line[2]
        magnets.share_date = line[3]
        magnets.save()
        magnet_count += 1
        result_msg.resource_count += 1
        # for property, value in vars(magnets).iteritems():
        #     print property, ": ", value
    message = "" + movie_info.no + " find: " + str(magnet_count) + " resource"
    print message
    return message
