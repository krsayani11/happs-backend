from .serializers import UserSerializer, FriendsSerializer
from rest_framework import routers, serializers, viewsets
from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Friends
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',
    	'username',
    	'user_id',
    	'authentication_token'
    	'picture')
	
class FriendsViewSet(viewsets.ModelViewSet):
	queryset = Friends.objects.all()
	serializer_class = FriendsSerializer
