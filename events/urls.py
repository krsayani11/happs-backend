from django.conf.urls import url

from . import views
from .views import (
	EventDetailAPIView,
	EventListAPIView,
	EventUpdateAPIView,
	EventDestroyAPIView,
	AttendeesUpdateAPIView,
	AttendeesDestroyAPIView,)

app_name = 'events'
urlpatterns = [
	#url(r'^$', EventListAPIView.as_view()),
	url(r'^(?P<pk>\d+)/edit/$', EventUpdateAPIView.as_view()),
	url(r'^(?P<pk>\d+)/destroy/$', EventDestroyAPIView.as_view()),
	url(r'^(?P<pk>\d+)/detail/$', EventDetailAPIView.as_view()),
	url(r'^attendees/(?P<pk>\d+)/edit/$', AttendeesUpdateAPIView.as_view()),
	url(r'^attendees/(?P<pk>\d+)/destroy/$', AttendeesDestroyAPIView.as_view()),
	
]