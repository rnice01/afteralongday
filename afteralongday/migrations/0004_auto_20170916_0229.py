# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-16 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afteralongday', '0003_auto_20170916_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bathbombs',
            name='image_url',
            field=models.TextField(default='/home/rob/PycharmProjects/afteralongday/afteralongday/afteralongday/assets/images/bathbombs/bathbomb_placeholder.jpg'),
        ),
    ]