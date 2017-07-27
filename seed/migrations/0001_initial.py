# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 00:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_url', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=255, null=True)),
                ('birth', models.CharField(max_length=12, null=True)),
                ('age', models.CharField(max_length=12, null=True)),
                ('heigth', models.CharField(max_length=12, null=True)),
                ('cup', models.CharField(max_length=12, null=True)),
                ('bust', models.CharField(max_length=12, null=True)),
                ('waist', models.CharField(max_length=12, null=True)),
                ('hips', models.CharField(max_length=12, null=True)),
                ('hometown', models.CharField(max_length=50, null=True)),
                ('hobby', models.CharField(max_length=50, null=True)),
                ('uncensored', models.CharField(default='n', max_length=2)),
                ('check_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Magnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1023)),
                ('file_name', models.CharField(max_length=1023)),
                ('size', models.CharField(max_length=12, null=True)),
                ('share_date', models.CharField(max_length=12, null=True)),
                ('magnet_url', models.CharField(max_length=1023)),
                ('hd', models.CharField(default='n', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='test', max_length=1023)),
                ('no', models.CharField(max_length=50)),
                ('movie_url', models.CharField(max_length=255)),
                ('movie_img_url', models.CharField(max_length=255, null=True)),
                ('date', models.CharField(max_length=12, null=True)),
                ('length', models.CharField(max_length=12, null=True)),
                ('director', models.CharField(max_length=50, null=True)),
                ('maker', models.CharField(max_length=50, null=True)),
                ('has_mask', models.CharField(default='y', max_length=2, null=True)),
                ('uncensored', models.CharField(default='n', max_length=2)),
                ('check_date', models.DateTimeField(null=True)),
                ('gid', models.CharField(max_length=255)),
                ('uc', models.CharField(max_length=2)),
                ('img', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie_Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seed.Actors')),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seed.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seed.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('series_url', models.CharField(max_length=1023)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tag_url', models.CharField(max_length=1023)),
            ],
        ),
        migrations.AddField(
            model_name='movie_tag',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seed.Tag'),
        ),
        migrations.AddField(
            model_name='movie',
            name='series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seed.Series'),
        ),
        migrations.AddField(
            model_name='magnet',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seed.Movie'),
        ),
    ]
