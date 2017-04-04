from django.conf.urls import url
from . import views
from .views import (
	UserDetailAPIView,
	UserUpdateAPIView,
	UserDestroyAPIView,
	FriendshipDetailAPIView,
	FriendshipUpdateAPIView,
	FriendshipDestroyAPIView,

	)

app_name = 'users'
urlpatterns = [
	url(r'^users/(?P<pk>\d+)/edit/$', UserUpdateAPIView.as_view()),
	url(r'^users/(?P<pk>\d+)/destroy/$', UserDestroyAPIView.as_view()),
	url(r'^users/(?P<pk>\d+)/detail/$', UserDetailAPIView.as_view()),
	


	]
