from __future__ import unicode_literals
from django.db import models

class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255, primary_key=True)
	user_id = models.BigIntegerField()
	authentication_token = models.CharField(max_length=255)
	# Profile picture

	def __str__(self):
		return self.name

class Friends(models.Model):
	created = models.DateTimeField(auto_now_add=True, editable=False)
	creator = models.ForeignKey(User, related_name="friendship_creator_set")

	# need to FIX this relationship (it's one-sided)
	# maybe I can add a query to filter all of a user's friends
	friend = models.ForeignKey(User, related_name="friend_set") 
