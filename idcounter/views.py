from django.http import HttpResponse
from django.http import JsonResponse
from django.db import DatabaseError


import json

from .models import IdCollection


def getUser(request):
    collection = IdCollection.objects.get(id=1)
    return JsonResponse({'response': collection.id_user})


def getEvent(request):
    try:
        collection = IdCollection.objects.get(id=1)
    except (IdCollection.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    return JsonResponse({'response': collection.id_event})


def getInvite(request):
    try:
        collection = IdCollection.objects.get(id=1)
    except (IdCollection.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    return JsonResponse({'response': collection.id_invite})
