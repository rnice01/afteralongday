# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-22 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afteralongday', '0010_auto_20170603_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bathbombs',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
