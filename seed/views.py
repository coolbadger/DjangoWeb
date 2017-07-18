# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from seed import models
from seed.crawler import process
import threading


# Create your views here.



def default(request):
    task = threading.Thread(target=process.update_censored)
    task.setDaemon(True)
    task.start()

    resp = render_to_response('index.html')
    return resp
