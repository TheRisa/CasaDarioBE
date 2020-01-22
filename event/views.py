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

def conncet():
    myclient = MongoClient(
            "mongodb+srv://TheRisa:admin1832@casadario-kzgcj.mongodb.net/test?retryWrites=true&w=majoritys")
    mydb = myclient["casadario"]
    return mydb


def getAllEvents(request, userNameInput):
    try:
        user = User.objects.get(userName=userNameInput)
        db = connect()
        inviteCol = db['invite_invite']
        invites = inviteCol.find_one()
    except(Invite.DoesNotExist, User.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    # response = []
    # test = invites.event
    # for invite in invites:
    #     event = Event.objects.get(id=invite.event)
    #     test = event.id
    #     tmpEvent = {
    #         'id': event.id,
    #         'name': event.name,
    #         'description': event.description,
    #         'place': event.place,
    #         'date': event.date,
    #         'initHour': event.initHour,
    #         'type': event.type,
    #         'creator': event.creator,
    #         'isConfirmed': isConfirmed
    #     }
    #     response.append(tmpEvent)
    # return JsonResponse({'response': response, 'user': user.id, 'prova': invites.event})
    return JsonResponse({'prova': invites.event})


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
        mydb = connect()
        mycol = mydb["event_event"]
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
