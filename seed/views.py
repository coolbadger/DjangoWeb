# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.utils.timezone import utc
from django.shortcuts import render, render_to_response
from seed import models
import threading

# Create your views here.


from seed.crawler.main import craw


def default(request):
    threads = []
    # censored = threading.Thread(target=craw, args=(r'https://www.seedmm.com/page/',))
    # uncensored = threading.Thread(target=craw, args=(r'https://www.seedmm.com/uncensored/page/',))

    # task = threading.Thread(target=craw, args=(r'https://www.seedmm.com/uncensored/star/l2r/',))

    task = threading.Thread(target=update_by_actors)
    task.setDaemon(True)
    task.start()

    # threads.append(task)

    # for thread in threads:
    #     thread.setDaemon(True)
    #     thread.start()

    resp = render_to_response('index.html', locals())
    return resp


def update_by_actors():
    for actor in models.Actors.objects.filter(check_date=None):
        url = actor.actor_url + r'/'
        craw(url)
        actor.check_date = datetime.datetime.now().replace(tzinfo=utc)
        actor.save()
    return ""
