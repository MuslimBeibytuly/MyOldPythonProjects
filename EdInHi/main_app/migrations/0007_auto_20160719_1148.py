# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-19 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20160714_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstractuser',
            name='city',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='abstractuser',
            name='country',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]