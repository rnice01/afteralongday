# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170529_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favorited',
            field=models.IntegerField(default=0),
        ),
    ]
