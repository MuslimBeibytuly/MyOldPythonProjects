# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-13 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialization',
            name='in_wishlist_of_users',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]