from django.http import HttpResponse
from django.http import JsonResponse
from django.db import DatabaseError
from django.core import serializers

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
        return JsonResponse({'response': ''})
    return JsonResponse({'response': {
        'userName': user.userName,
        'password': user.password,
        'firstName': user.firstName,
        'lastName': user.lastName,
        'totalPoint': user.totalPoint,
        'mothPoint': user.monthPoint,
        'gayPoint': user.gayPoint
    }})


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
    try:
        user.save()
    except DatabaseError:
        return JsonResponse({'response': False})
    return JsonResponse({'response': True})
