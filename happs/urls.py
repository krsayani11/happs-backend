"""happs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers, serializers, viewsets
from django.conf.urls import include, url
from django.contrib import admin
from users import views as uviews
from events import views as eviews
from photos import views as pviews

router = routers.DefaultRouter()
router.register(r'api/users', uviews.UserViewSet)
router.register(r'api/events', eviews.EventViewSet)
router.register(r'api/photos', pviews.PhotoViewSet)
router.register(r'api/friendships', uviews.FriendshipViewSet)
router.register(r'api/attendees', eviews.AttendeesViewSet)
router.register(r'api/invitation', eviews.InvitationViewSet)
admin.autodiscover()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/events/', include("events.urls", namespace='events-api')),
    url(r'^api/photos/', include("photos.urls", namespace='photos-api')),
    url(r'^api/attendees/(?P<pk>\d+)/edit/$', eviews.AttendeesUpdateAPIView.as_view()),
    url(r'^api/attendees/(?P<pk>\d+)/destroy/$', eviews.AttendeesDestroyAPIView.as_view()),
    url(r'^api/invitation/(?P<pk>\d+)/edit/$', eviews.InvitationUpdateAPIView.as_view()),
    url(r'^api/invitation/(?P<pk>\d+)/destroy/$', eviews.InvitationDestroyAPIView.as_view()),
    url(r'^api/friendships/(?P<pk>\d+)/edit/$', uviews.FriendshipUpdateAPIView.as_view()),
    url(r'^api/friendships/(?P<pk>\d+)/destroy/$', uviews.FriendshipDestroyAPIView.as_view()),
    url(r'^api/friendships/(?P<pk>\d+)/detail/$', uviews.FriendshipDetailAPIView.as_view()),
    url(r'^api/users/(?P<pk>\d+)/edit/$', uviews.UserUpdateAPIView.as_view()),
    url(r'^api/users/(?P<pk>\d+)/destroy/$', uviews.UserDestroyAPIView.as_view()),
    url(r'^api/users/(?P<pk>\d+)/detail/$', uviews.UserDetailAPIView.as_view()),]

urlpatterns += staticfiles_urlpatterns()
