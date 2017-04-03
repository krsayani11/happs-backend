from .serializers import PhotoSerializer
from rest_framework import routers, serializers, viewsets
from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
        DestroyAPIView,
        ListAPIView,
        UpdateAPIView,
        RetrieveAPIView)

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('username',
        'created',
        'event_id',
        'datafile')

class PhotoDetailAPIView(RetrieveAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoUpdateAPIView(UpdateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoDestroyAPIView(DestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer