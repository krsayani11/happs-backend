# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 08:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170403_0818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendship',
            name='data_joined',
        ),
    ]