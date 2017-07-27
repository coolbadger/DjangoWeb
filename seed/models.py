# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Series(models.Model):
    name = models.CharField(max_length=1023)
    series_url = models.TextField()

    image_url = models.CharField(max_length=255, null=True)
    check_date = models.DateTimeField(null=True)
    pass


class Movie(models.Model):
    title = models.TextField()
    no = models.CharField(max_length=50)
    movie_url = models.CharField(max_length=255)
    movie_img_url = models.CharField(max_length=255, null=True)
    date = models.CharField(max_length=12, null=True)
    length = models.CharField(max_length=12, null=True)
    director = models.CharField(max_length=50, null=True)
    maker = models.CharField(max_length=50, null=True)
    series = models.ForeignKey(Series, null=True)
    has_mask = models.CharField(max_length=2, null=True, default='y')
    uncensored = models.CharField(max_length=2, default='n')
    check_date = models.DateTimeField(null=True)

    gid = models.CharField(max_length=255)
    uc = models.CharField(max_length=2)
    img = models.CharField(max_length=255)

    pass


class Tag(models.Model):
    name = models.TextField()
    tag_url = models.TextField()

    pass


class Actors(models.Model):
    actor_url = models.CharField(max_length=255)
    name = models.CharField(max_length=1023)
    image_url = models.TextField(null=True)
    birth = models.CharField(max_length=12, null=True)
    age = models.CharField(max_length=12, null=True)
    heigth = models.CharField(max_length=12, null=True)
    cup = models.CharField(max_length=12, null=True)
    bust = models.CharField(max_length=12, null=True)
    waist = models.CharField(max_length=12, null=True)
    hips = models.CharField(max_length=12, null=True)
    hometown = models.CharField(max_length=50, null=True)
    hobby = models.CharField(max_length=50, null=True)
    uncensored = models.CharField(max_length=2, default='n')
    check_date = models.DateTimeField(null=True)

    pass


class Magnet(models.Model):
    movie = models.ForeignKey(Movie, null=True)
    title = models.TextField()
    file_name = models.TextField()
    size = models.CharField(max_length=12, null=True)
    share_date = models.CharField(max_length=12, null=True)
    magnet_url = models.TextField()
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
