# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 02:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('afteralongday', '0008_auto_20170601_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='bathbombs',
            name='invoice',
        ),
        migrations.AddField(
            model_name='order',
            name='bathbomb',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='afteralongday.BathBombs'),
        ),
        migrations.AddField(
            model_name='order',
            name='invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='afteralongday.Invoice'),
        ),
    ]