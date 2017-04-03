from rest_framework import viewsets, status, permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.response import Response
from .models import Event, Attendees
from rest_framework.generics import (
        DestroyAPIView,
        ListAPIView,
        UpdateAPIView,
        RetrieveAPIView)
from django.http import HttpResponse
from .serializers import EventSerializer, AttendeesSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('event_name', 
            'address', 
            'date', 
            'start_time', 
            'end_time', 
            'host', 
            'description',
            'private',
            'event_id',
            'place_name',)

    @detail_route(methods=['post'])
    def addEvent(self, request):
        serializer = EventSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def search(request):
        queryset_list = Event.objects.all() 
        query = request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(event_name__icontains=query),
                    Q(date__icontains=query),
                    Q(start_time__icontains=query),
                    Q(end_time__icontains=query),
                    Q(host__icontains=query),
                    Q(description__icontains=query),
                    )
        return queryset_list

    
def event(request, pk):
    queryset = Event.objects.get(pk)
    serializer = EventSerializer
    return Response(serializer.data)



class EventDetailAPIView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventUpdateAPIView(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDestroyAPIView(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('event_name', 
            'address', 
            'date', 
            'start_time', 
            'end_time', 
            'host', 
            'description',
            'picture',
            'private'
            'place_name',)

class AttendeesViewSet(viewsets.ModelViewSet):
    queryset = Attendees.objects.all()
    serializer_class = AttendeesSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('event_id', 'attendees')

class AttendeesUpdateAPIView(UpdateAPIView):
    queryset = Attendees.objects.all()
    serializer_class = AttendeesSerializer

class AttendeesDestroyAPIView(DestroyAPIView):
    queryset = Attendees.objects.all()
    serializer_class = AttendeesSerializer