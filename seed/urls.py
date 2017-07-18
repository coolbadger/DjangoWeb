#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name	: urls
# Author		: badger
# Created		: 2017/7/13
# Description	: 
from django.conf.urls import url, include
from seed import views

urlpatterns = [
    url(r'^index/', views.default),
    url(r'^process_start/', views.process_start),
    url(r'^process_stop/', views.process_stop),
]
