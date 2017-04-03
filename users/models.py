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



class Friendship(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="friendship_creator_set")
    friend = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="friend_set")
    status = models.CharField(max_length=64,)

    def __str__(self):
        return self.person