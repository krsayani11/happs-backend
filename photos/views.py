from .serializers import PhotoSerializer
from rest_framework import routers, serializers, viewsets
from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
from django_filters.rest_framework import DjangoFilterBackend

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('username',
        'created',
        'event_id',
        'datafile')
