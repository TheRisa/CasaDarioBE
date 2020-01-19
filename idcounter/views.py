from django.http import HttpResponse
from django.http import JsonResponse
from django.db import DatabaseError


import json

from .models import Collection


def getUser(request):
    try:
        collection = Collection.objects.get(id=1)
    except (Collection.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    return JsonResponse({'response': collection.id_user})


def getEvent(request):
    try:
        collection = Collection.objects.get(id=1)
    except (Collection.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    return JsonResponse({'response': collection.id_event})


def getInvite(request):
    try:
        collection = Collection.objects.get(id=1)
    except (Collection.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    return JsonResponse({'response': collection.id_invite})
