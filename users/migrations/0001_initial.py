# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 05:21
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('status', models.CharField(max_length=64)),
                ('friendship_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('user_id', models.BigIntegerField()),
                ('authentication_token', models.CharField(max_length=255)),
                ('picture', models.TextField(validators=[django.core.validators.URLValidator()])),
            ],
        ),
        migrations.AddField(
            model_name='friendship',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_set', to='users.User'),
        ),
        migrations.AddField(
            model_name='friendship',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship_creator_set', to='users.User'),
        ),
    ]
