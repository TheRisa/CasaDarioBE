from django.http import HttpResponse
from django.http import JsonResponse
from django.db import DatabaseError
from django.core import serializers

import json
import urllib.request

from .models import Event


def api(request):
    return HttpResponse("Benvenuto nel back office di CasaDario, sezione Event api.")


def getAllEvents(request):
    try:
        events = Event.objects.all()
    except(Event.DoesNotExist, DataBaseError):
        return JsonResponse({'response': False})
    response = []
    for event in events:
        tmpEvent = {
            'name': event.name,
            'description': event.description,
            'place': event.place,
            'date': event.date,
            'initHour': event.initHour,
            'type': event.type
        }
        response.append(tmpEvent)
    return JsonResponse({'response': response})
