from django.http import HttpResponse
from django.http import JsonResponse
from django.db import DatabaseError
from django.core import serializers

import datetime

import json
import urllib.request

from .models import User

"""
/api/user/
Home di api user, non fa nulla tranne render
"""


def api(request):
    return HttpResponse("Benvenuto nel back office di CasaDario, sezione User api.")


"""
/api/user/login/username/password
Controlla che username e passwrod corrispondano
Return true se corrispondono
"""


def logIn(request, userName, psw):
    try:
        user = User.objects.get(userName=userName)
        if (user.password == psw):
            return JsonResponse({'response': True})
        else:
            return JsonResponse({'response': False})
    except (User.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})


"""
/api/user/getuser/<username>
Cerca username nel db
return json di tutti i dati dell'utente
"""


def getUser(request, userName):
    try:
        user = User.objects.get(userName=userName)
    except (User.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    return JsonResponse({'response': {
        'userName': user.userName,
        'description': user.description,
        'firstName': user.firstName,
        'id': user.id,
        'lastName': user.lastName,
        'totalPoint': user.totalPoint,
        'monthPoint': user.monthPoint,
        'gayPoint': user.gayPoint
    }})


"""
/api/user/getalluser
Restituisce tutti gli utenti
return json di tutti i dati degli utenti
"""


def getAllUsers(request):
    try:
        users = User.objects.all()
    except (User.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    returnValue = []
    for user in users:
        tmpuser = {
            'userName': user.userName,
            'firstName': user.firstName,
            'lastName': user.lastName,
            'totalPoint': user.totalPoint,
            'monthPoint': user.monthPoint,
            'description': user.description,
            'id': user.id,
            'gayPoint': user.gayPoint,
            'profileImg': user.profileImg
        }
        returnValue.append(tmpuser)
    return JsonResponse({'response': returnValue})


"""
/api/user/createuser/<username>/<password>/<firstName>/<lastName>
Aggiunge al db un nuovo user con i dati passati
return true se l'utente è stato inserito
"""


def createUser(request, userName, psw, firstName, lastName):
    user = User()
    user.firstName = firstName
    user.lastName = lastName
    user.userName = userName
    user.password = psw
    user.description = ''
    user.gayPoint = 0
    user.totalPoint = 0
    user.monthPoint = 0
    user.profileImg = 'https: // polar-tundra-64747.herokuapp.com/static/image/casadario/profile/profile-default.png'
    user.lastDate = None
    try:
        user.save()
    except DatabaseError:
        return JsonResponse({'response': False})
    return JsonResponse({'response': True})


def getLastLogin(request, userName):
    try:
        user = User.objects.get(userName=userName)
    except (User.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    return JsonResponse({'response': user.lastDate})


def updateLastLogin(request, userName):
    try:
        user = User.objects.get(userName=userName)
        user.lastDate = datetime.date.today()
        user.save()
    except (User.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    return JsonResponse({'response': user.lastDate})


def updateTotalPoint(request, userName):
    try:
        user = User.objects.get(userName=userName)
        user.totalPoint = user.totalPoint + 1
        user.monthPoint = user.monthPoint + 1
        user.save()
    except (User.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    return JsonResponse({'response': user.totalPoint})


def getProfileImg(request, userName):
    try:
        user = User.objects.get(userName=userName)
    except (User.DoesNotExist, DatabaseError):
        return JsonResponse({'response': False})
    return JsonResponse({'response': user.profileImg})
