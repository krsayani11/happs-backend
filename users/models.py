from __future__ import unicode_literals
from django.db import models
from django.core.validators import URLValidator

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, primary_key=True)
    user_id = models.BigIntegerField()
    authentication_token = models.CharField(max_length=255)
    picture = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.username

class Friends(models.Model):
    members = models.ManyToManyField(User, through='Friendship')
    status = models.CharField(max_length=64)

class Friendship(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    friends = models.ForeignKey(Friends, on_delete=models.CASCADE)
    status = models.CharField(max_length=64)