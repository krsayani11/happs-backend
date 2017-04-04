# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 19:54
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('datafile', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('photo_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('username', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
    ]
