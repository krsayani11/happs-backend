from .serializers import UserSerializer, FriendshipSerializer
from rest_framework import routers, serializers, viewsets
from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Friendship
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
        DestroyAPIView,
        ListAPIView,
        UpdateAPIView,
        RetrieveAPIView)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',
        'username',
        'user_id',
        'picture')
    
class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FriendshipViewSet(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('person', 'friend', 'status')

class FriendshipDetailAPIView(RetrieveAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer

class FriendshipUpdateAPIView(UpdateAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer

class FriendshipDestroyAPIView(DestroyAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer
