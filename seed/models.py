# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

# 做个梦呗
class dream(models.Model):
    title = models.CharField(max_length=50)
    sn = models.CharField(max_length=12)
    content = models.CharField(max_length=255)
    tag = models.CharField(max_length=10)
    date = models.DateField()
    state = models.CharField(max_length=2)
    pass


class Movie(models.Model):
    title = models.CharField(max_length=255)
    no = models.CharField(max_length=50)
    movie_url = models.CharField(max_length=255)
    date = models.CharField(max_length=12, null=True)
    length = models.CharField(max_length=12, null=True)
    director = models.CharField(max_length=50, null=True)
    maker = models.CharField(max_length=50, null=True)
    has_mask = models.CharField(max_length=2, null=True, default='y')
    uncensored = models.CharField(max_length=2, default='n')

    gid = models.CharField(max_length=255)
    uc = models.CharField(max_length=2)
    img = models.CharField(max_length=255)

    pass


class Tag(models.Model):
    name = models.CharField(max_length=50)
    tag_url = models.CharField(max_length=255)

    pass


class Actors(models.Model):
    actor_url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    birth = models.CharField(max_length=12)
    heigth = models.CharField(max_length=12)
    cup = models.CharField(max_length=12)
    bust = models.CharField(max_length=12)
    waist = models.CharField(max_length=12)
    hips = models.CharField(max_length=12)
    hometown = models.CharField(max_length=50, null=True)
    hobby = models.CharField(max_length=50, null=True)
    uncensored = models.CharField(max_length=2, default='n')

    pass


class Magnet(models.Model):
    movie = models.ForeignKey(Movie, null=True)
    title = models.CharField(max_length=255)
    file_name = models.CharField(max_length=1023)
    size = models.CharField(max_length=12)
    share_date = models.CharField(max_length=12)
    magnet_url = models.CharField(max_length=1023)
    hd = models.CharField(max_length=2, default='n')

    pass


# 影片对应关系 标签与演员
class Movie_Tag(models.Model):
    movie = models.ForeignKey(Movie, null=True)
    tag = models.ForeignKey(Tag, null=True)
    pass


class Movie_Actor(models.Model):
    movie = models.ForeignKey(Movie, null=True)
    actor = models.ForeignKey(Actors, null=True)
    pass
