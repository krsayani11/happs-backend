from __future__ import unicode_literals
from django.db import models
from django.core.validators import URLValidator

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    user_id = models.BigIntegerField()
    authentication_token = models.CharField(max_length=255)
    picture = models.TextField(validators=[URLValidator()])
    user_identification = models.AutoField(primary_key=True)

    def __str__(self):
        return self.username



class Friendship(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="friendship_creator_set")
    friend = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="friend_set")
    status = models.CharField(max_length=64,)
    friendship_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.person