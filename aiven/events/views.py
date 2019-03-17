from django.shortcuts import render

# Create your views here.
from .kafkaConfig import producer,consumer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import EventSerializer
from .models import Event



class events(APIView):
    def get(self, request, *args, **kwargs):
        #events=Event.objects.all();
        events=consumer('events')
        serialized_events=[]
        for event in events:
            serializer= EventSerializer(event)
            serialized_events.append(serializer.data)
        return Response(serialized_events)


    def post(self, request, *args, **kwargs):
        serialized_Event = EventSerializer(data=request.data)
        if not serialized_Event.is_valid():
            return Response("Not valida data")
        serialized_Event.save()
        producer.send('events',value=serialized_Event.data)
        producer.flush()
        return Response(serialized_Event.data)
