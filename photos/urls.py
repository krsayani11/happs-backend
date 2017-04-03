from django.conf.urls import url
from . import views
from .views import (
	PhotoDetailAPIView,
	PhotoUpdateAPIView,
	PhotoDestroyAPIView,)


app_name = 'photos'
urlpatterns = [
	url(r'^(?P<pk>\d+)/edit/$', PhotoUpdateAPIView.as_view()),
	url(r'^(?P<pk>\d+)/destroy/$', PhotoDestroyAPIView.as_view()),
	url(r'^(?P<pk>\d+)/detail/$', PhotoDetailAPIView.as_view()),]