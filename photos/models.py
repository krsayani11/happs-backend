from __future__ import unicode_literals

from django.db import models
from django.core.validators import URLValidator

# Create your models here.

class Photo(models.Model):
	username = models.ForeignKey(
         'users.user',
         on_delete=models.CASCADE,
         default = None,)
	created = models.DateTimeField(auto_now_add=True)
	event_id = event_id = models.ForeignKey(
         'events.event',
         on_delete=models.CASCADE,
         default = None,)
	datafile = models.TextField(validators=[URLValidator()])

	def __str__(self):
		return self.event_i