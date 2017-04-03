from __future__ import unicode_literals
from django.db import models
from django.core.validators import URLValidator


# Create your models here.
class Event(models.Model):
	event_name = models.CharField(max_length=255)
	place_name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	date = models.DateField()
	start_time = models.TimeField()
	end_time = models.TimeField()
	host = models.ForeignKey('users.User', related_name = "for_host", on_delete=models.CASCADE, default = None,)
	description = models.TextField()
	longitude = models.CharField(max_length=255)
	latitude = models.CharField(max_length=255)
	picture = models.TextField(validators=[URLValidator()])
	event_id = models.AutoField(primary_key=True)
	private = models.BooleanField()

	def __str__(self):
		return self.event_name


class Attendees(models.Model):
    event_id = models.ForeignKey(
         'event',
         on_delete=models.CASCADE,
         default = None,)
    attendees = models.ManyToManyField('users.User')

    def __str__(self):
        return self.event_id