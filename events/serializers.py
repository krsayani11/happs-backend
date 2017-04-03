from .models import Event
from users.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'event_name', 'address', 'date', 'start_time', 'end_time', 'host', 
                  'description','longitude','latitude', 'picture')