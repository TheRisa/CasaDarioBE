from django.http import HttpResponse
from django.http import JsonResponse
from django.db import DatabaseError
from django.core import serializers

import json
import urllib.request

from .models import Invite
from event.models import Event
from user.models import User


def api(request):
    return HttpResponse("Benvenuto nel back office di CasaDario, sezione Invite api.")


def addInvite(request, userId, eventId):
    try:
        event = Event.objects.get(id=eventId)
        user = User.objects.get(id=userId)
        invite = Invite()
        invite.event = event
        invite.user = user
        invite.save()
    except (Invite.DoesNotExist, User.DoesNotExist, Event.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    return JsonResponse({'response': True})


def getInvitedUser(request, eventId):
    try:
        event = Event.objects.get(id=eventId)
        invites = Invite.objects.filter(event=event)
    except (Event.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    response = []
    for invite in invites:
        response.append(invite.user.userName)
    return JsonResponse({'response': response})


def getInvitedAndConfirmedUser(request, eventId):
    try:
        event = Event.objects.get(id=eventId)
        invites = Invite.objects.filter(event=event)
    except (Event.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    response = []
    for invite in invites:
        if (invite.isConfirmed):
            response.append(invite.user.userName)
    return JsonResponse({'response': response})


def deleteOldInvites(request, eventId):
    try:
        event = Event.objects.get(id=eventId)
        invites = Invite.objects.filter(event=event)
    except (Event.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    for invite in invites:
        invite.delete()
    return JsonResponse({'response': True})


def setIsConfirmed(request, confirmation, eventId, userId):
    try:
        event = Event.objects.get(id=eventId)
        user = User.objects.get(id=userId)
        invites = Invite.objects.filter(event=event, user=user)
    except (Event.DoesNotExist, User.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    for invite in invites:
        invite.isConfirmed = confirmation
        invite.save()
    return JsonResponse({'response': True})
