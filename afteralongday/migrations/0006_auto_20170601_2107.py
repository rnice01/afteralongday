# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 02:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('afteralongday', '0005_auto_20170530_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='bath_bombs',
        ),
        migrations.AddField(
            model_name='bathbombs',
            name='invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='afteralongday.Invoice'),
        ),
    ]
