# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-05 18:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('work', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('gender', models.BooleanField(default=True)),
                ('send_email', models.BooleanField(default=True)),
                ('home', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='Images/')),
                ('data_of_birth', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_id', models.IntegerField(blank=True, null=True)),
                ('gem_type', models.IntegerField(blank=True, null=True)),
                ('gems', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='abstractuser',
            name='codes',
            field=models.ManyToManyField(blank=True, to='main_app.Code'),
        ),
        migrations.AddField(
            model_name='abstractuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]