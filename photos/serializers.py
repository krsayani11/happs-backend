from .models import Photo
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ('username', 'created', 'event_id', 'datafile',)