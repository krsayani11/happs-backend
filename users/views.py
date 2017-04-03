from .serializers import UserSerializer, FriendsSerializer
from rest_framework import routers, serializers, viewsets
from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Friends

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	
class FriendsViewSet(viewsets.ModelViewSet):
	queryset = Friends.objects.all()
	serializer_class = FriendsSerializer
