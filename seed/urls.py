#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name	: urls
# Author		: badger
# Created		: 2017/7/13
# Description	: 
from django.conf.urls import url, include
from seed import views

urlpatterns = [
    url(r'^(\d{0,10})$', views.movie),
    url(r'^actor/(\d{1,10})', views.actor_resource),
    url(r'^actor_page/(\d{0,10})', views.actors),
    url(r'^series/(\d{1,10})', views.series_resource),
    url(r'^series_page/(\d{0,10})', views.series_page),
    url(r'^process_start/', views.process_start),
    url(r'^process_stop/', views.process_stop),
]
