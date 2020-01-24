from django.http import HttpResponse
from django.http import JsonResponse
from django.db import DatabaseError
from django.core import serializers

import json
import urllib.request

from .models import Invite
from event.models import Event
from user.models import User

from pymongo.errors import BulkWriteError
from pymongo import MongoClient


def api(request):
    return HttpResponse("Benvenuto nel back office di CasaDario, sezione Invite api.")

def connect():
    myclient = MongoClient(
            "mongodb+srv://TheRisa:admin1832@casadario-kzgcj.mongodb.net/test?retryWrites=true&w=majority")
    mydb = myclient["casadario"]
    return mydb


def addInvite(request, userId, eventId):
    # Metodo mysql
    # try:
    #     event = Event.objects.get(id=eventId)
    #     user = User.objects.get(id=userId)
    #     invite = Invite()
    #     invite.event = event
    #     invite.user = user
    #     invite.save()
    # except (Invite.DoesNotExist, User.DoesNotExist, Event.DoesNotExist, DatabaseError):
    #     return JsonResponse({'response': False})
    # return JsonResponse({'response': True})

    # Metodo mongodb
    try:
        db = connect()
        inviteCol = db['invite_invite']
        list = [{"event": eventId, "user": userId, "isConfirmed": False}]
        inviteCol.insert_many(list)
    except BulkWriteError:
        return JsonResponse({'response': False})
    return JsonResponse({'response': True})


def getInvitedUser(request, eventId):
    # Metodo mysql
    # try:
    #     event = Event.objects.get(id=eventId)
    #     invites = Invite.objects.filter(event=event)
    # except (Event.DoesNotExist, DatabaseError):
    #     return JsonResponse({'response': False})
    # response = []
    # for invite in invites:
    #     response.append(invite.user.userName)
    # return JsonResponse({'response': response})

    # Metodo mongodb
    response = []
    try:
        db = connect()
        inviteCol = db['invite_invite']
        invites = inviteCol.find({"event": int(eventId)})
        userCol = db['user_user']
        for invite in invites:
            user = userCol.find_one({"id": int(invite['user'])})
            response.append(user['userName'])
    except (Event.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    return JsonResponse({'response': response})



def getInvitedAndConfirmedUser(request, eventId):
    # Metodo mysql
    # try:
    #     event = Event.objects.get(id=eventId)
    #     invites = Invite.objects.filter(event=event)
    # except (Event.DoesNotExist, DatabaseError):
    #     return JsonResponse({'response': False})
    # response = []
    # for invite in invites:
    #     if (invite.isConfirmed):
    #         response.append(invite.user.userName)
    # return JsonResponse({'response': response})

    response = []
    try:
        db = connect()
        inviteCol = db['invite_invite']
        invites = inviteCol.find({"event": int(eventId)})
        userCol = db['user_user']
        for invite in invites:
            if (invite['isConfirmed'] and invite['isConfirmed'] != 'False'):
                user = userCol.find_one({"id": invite['user']})
                response.append(user['userName'])
    except (Event.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    return JsonResponse({'response': response})


def deleteOldInvites(request, eventId):
    # Metodo mysql
    # try:
    #     event = Event.objects.get(id=eventId)
    #     invites = Invite.objects.filter(event=event)
    # except (Event.DoesNotExist, DatabaseError):
    #     return JsonResponse({'response': False})
    # for invite in invites:
    #     invite.delete()
    # return JsonResponse({'response': True})

    # Metodo mongodb
    try:
        db = connect()
        inviteCol = db['invite_invite']
        inviteCol.delete_many({"event": int(eventId)})
    except BulkWriteError:
        return JsonResponse({'response': False})
    return JsonResponse({'response': True})


def setIsConfirmed(request, confirmation, eventId, userName):
    # Metodo mysql
    # try:
    #     event = Event.objects.get(id=eventId)
    #     user = User.objects.get(userName=userName)
    #     invites = Invite.objects.filter(event=event, user=user)
    # except (Event.DoesNotExist, User.DoesNotExist, DatabaseError):
    #     return JsonResponse({'response': False})
    # for invite in invites:
    #     invite.isConfirmed = confirmation
    #     invite.save()
    # return JsonResponse({'response': True})

    # Metodo mongodb
    try:
        db = connect()
        inviteCol = db['invite_invite']
        userCol = db['user_user']
        user = userCol.find_one({"userName": userName})
        inviteCol.update_one({"event": int(eventId), "user": user['id']},
            {"$set": {"isConfirmed": confirmation}})
    except BulkWriteError:
        return JsonResponse({'response': False})
    return JsonResponse({'response': True})
