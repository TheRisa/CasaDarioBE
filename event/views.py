from django.http import HttpResponse
from django.http import JsonResponse
from django.db import DatabaseError
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes

import json
import urllib.request

from invite.models import Invite
from .models import Event
from idcounter.models import IdCollection
from user.models import User

from pymongo.errors import BulkWriteError
from pymongo import MongoClient


def api(request):
    return HttpResponse("Benvenuto nel back office di CasaDario, sezione Event api.")


def getAllEvents(request, userNameInput):
    try:
        response = []
        user = User.objects.get(userName=userNameInput)
        invites = Invite.objects.filter(user=user.userName)
    except(invites.DoesNotExist, User.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    response = []
    for invite in invites:
        tmpEvent = {
            'id': invite.event.id,
            'name': invite.event.name,
            'description': invite.event.description,
            'place': invite.event.place,
            'date': invite.event.date,
            'initHour': invite.event.initHour,
            'type': invite.event.type,
            'creator': invite.event.creator.userName,
            'isConfirmed': invite.isConfirmed
        }
        response.append(tmpEvent)
    return JsonResponse({'response': response, 'user': user.userName})


@api_view(['POST'])
@parser_classes([JSONParser])
def createEvent(request):
    #  Metodo per mysql
    # try:
    #     event = Event()
    #     event.name = request.data['name']
    #     event.description = request.data['description']
    #     event.place = request.data['place']
    #     event.date = request.data['date']
    #     event.initHour = request.data['initHour']
    #     event.type = request.data['type']
    #     user = User.objects.get(userName=request.data['creator'])
    #     event.creator = user
    #     event.save()

    # except (DatabaseError):
    #     return JsonResponse({'response': False})
    # return JsonResponse({'response': event.id})

    # Metodo per mongodb

    try:
        myclient = MongoClient(
            "mongodb+srv://TheRisa:admin1832@casadario-kzgcj.mongodb.net/test?retryWrites=true&w=majoritys")
        mydb = myclient["casadario"]
        mycol = mydb["askme_todo"]
        # TODO: da finire
        mylist = [
            {"name": request.data['name'], "description": request.data['description'],
                "place": request.data['place'], "date": request.data['date'],
                "initHour": request.data['initHour'], "type": request.data['type'],
                "creator": request.data['name']}

        ]
        mycol.insert_many(mylist)
    except BulkWriteError as bwe:
        return JsonResponse({'response': bwe.details["nInserted"] > 0})
    return JsonResponse({'response': True})


@api_view(['POST'])
@parser_classes([JSONParser])
def updateEvent(request, eventId):
    try:
        event = Event.objects.get(id=eventId)
        event.name = request.data['name']
        event.description = request.data['description']
        event.place = request.data['place']
        event.date = request.data['date']
        event.initHour = request.data['initHour']
        event.type = request.data['type']
        user = User.objects.get(userName=request.data['creator'])
        event.creator = user
        event.save()

    except (DatabaseError):
        return JsonResponse({'response': False})
    return JsonResponse({'response': event.id})
