from .models import Event, Attendees
from users.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class AttendeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendees
        fields = '__all__'
