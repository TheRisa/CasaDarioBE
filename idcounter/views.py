from django.http import HttpResponse
from django.http import JsonResponse
from django.db import DatabaseError


import json

from pymongo import MongoClient
from pymongo.errors import BulkWriteError

import pymongo
from bson.json_util import dumps

from .models import IdCollection

def conncet():
    myclient = MongoClient(
            "mongodb+srv://TheRisa:admin1832@casadario-kzgcj.mongodb.net/test?retryWrites=true&w=majority")
    mydb = myclient["casadario"]
    mycol = mydb["idcounter_idcollection"]
    return mycol


def getUser(request):
    try:
        mycol = conncet()
        collection = mycol.find_one()
    except (IdCollection.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    return JsonResponse({'response': collection['id_user']})


def incrementUser(request):
    # Metodo mysql
    # try:
    #     collection = IdCollection.objects.get(id=1)
    #     collection.id_user = collection.id_user + 1
    #     collection.save()
    # except (IdCollection.DoesNotExist, DatabaseError):
    #     return JsonResponse({'response': False})
    # return JsonResponse({'response': collection.id_user})

    # Metodo mongodb
    try:
        mycol = conncet()
        collection = mycol.find_one()
        mycol.update_one(
            {"collection_id": 1}, {"$set": {"id_user": collection["id_user"] + 1}})
    except BulkWriteError:
        return JsonResponse({'response': False})
    return JsonResponse({'response': True})


def getEvent(request):
    try:
        mycol = conncet()
        collection = mycol.find_one()
    except (IdCollection.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    return JsonResponse({'response': collection['id_event']})


def incrementEvent(request):
    # Metodo mysql
    # try:
    #     collection = IdCollection.objects.get(id=1)
    #     collection.id_event = collection.id_event + 1
    #     collection.save()
    # except (IdCollection.DoesNotExist, DatabaseError):
    #     return JsonResponse({'response': False})
    # return JsonResponse({'response': collection.id_event})

    # Metodo mongodb
    try:
        mycol = conncet()
        collection = mycol.find_one()
        mycol.update_one(
            {"collection_id": 1}, {"$set": {"id_event": collection["id_event"] + 1}})
    except BulkWriteError:
        return JsonResponse({'response': False})
    return JsonResponse({'response': True})


def getInvite(request):
    try:
        mycol = conncet()
        collection = mycol.find_one()
    except (IdCollection.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    return JsonResponse({'response': collection['id_invite']})


def incrementInvite(request):
    # Metodo mysql
    # try:
    #     collection = IdCollection.objects.get(id=1)
    #     collection.id_invite = collection.id_invite + 1
    #     collection.save()
    # except (IdCollection.DoesNotExist, DatabaseError):
    #     return JsonResponse({'response': False})
    # return JsonResponse({'response': collection.id_invite})

    # Metodo mongodb
    try:
        mycol = conncet()
        collection = mycol.find_one()
        mycol.update_one(
            {"collection_id": 1}, {"$set": {"id_invite": collection["id_invite"] + 1}})
    except BulkWriteError:
        return JsonResponse({'response': False})
    return JsonResponse({'response': True})
