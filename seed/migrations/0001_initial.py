# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 10:22
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
                ('birth', models.CharField(max_length=12)),
                ('heigth', models.CharField(max_length=12)),
                ('cup', models.CharField(max_length=12)),
                ('bust', models.CharField(max_length=12)),
                ('waist', models.CharField(max_length=12)),
                ('hips', models.CharField(max_length=12)),
                ('hometown', models.CharField(max_length=50, null=True)),
                ('hobby', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('sn', models.CharField(max_length=12)),
                ('content', models.CharField(max_length=255)),
                ('tag', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('state', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Magnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file_name', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=12)),
                ('share_date', models.CharField(max_length=12)),
                ('magnet_url', models.CharField(max_length=1023)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('no', models.CharField(max_length=50)),
                ('movie_url', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=12, null=True)),
                ('length', models.CharField(max_length=12, null=True)),
                ('director', models.CharField(max_length=50, null=True)),
                ('maker', models.CharField(max_length=50, null=True)),
                ('has_mask', models.CharField(max_length=2, null=True)),
                ('gid', models.CharField(max_length=50)),
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
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tag_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='movie_tag',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seed.Tag'),
        ),
        migrations.AddField(
            model_name='magnet',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seed.Movie'),
        ),
    ]