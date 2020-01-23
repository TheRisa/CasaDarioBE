from django.http import HttpResponse
from django.http import JsonResponse
from django.db import DatabaseError
from django.core import serializers

import datetime

import json
import urllib.request

from pymongo.errors import BulkWriteError
from pymongo import MongoClient

from .models import User
from idcounter.models import IdCollection


"""
/api/user/
Home di api user, non fa nulla tranne render
"""


def api(request):
    return HttpResponse("Benvenuto nel back office di CasaDario, sezione User api.")

def conncet():
    myclient = MongoClient(
            "mongodb+srv://TheRisa:admin1832@casadario-kzgcj.mongodb.net/test?retryWrites=true&w=majority")
    mydb = myclient["casadario"]
    return mydb


"""
/api/user/login/username/password
Controlla che username e passwrod corrispondano
Return true se corrispondono
"""


def logIn(request, userName, psw):
    try:
        user = User.objects.get(userName=userName)
        if (user.password == psw):
            return JsonResponse({"response": True})
        else:
            return JsonResponse({"response": False})
    except (User.DoesNotExist, DatabaseError):
        return JsonResponse({"response": False})


"""
/api/user/getuser/<username>
Cerca username nel db
return json di tutti i dati dell"utente
"""


def getUser(request, userName):
    try:
        user = User.objects.get(userName=userName)
    except (User.DoesNotExist, DatabaseError):
        return JsonResponse({"response": False})
    return JsonResponse({"response": {
        "userName": user.userName,
        "description": user.description,
        "firstName": user.firstName,
        "id": user.id,
        "lastName": user.lastName,
        "totalPoint": user.totalPoint,
        "monthPoint": user.monthPoint,
        "gayPoint": user.gayPoint
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
        return JsonResponse({"response": False})
    returnValue = []
    for user in users:
        tmpuser = {
            "userName": user.userName,
            "firstName": user.firstName,
            "lastName": user.lastName,
            "totalPoint": user.totalPoint,
            "monthPoint": user.monthPoint,
            "description": user.description,
            "id": user.id,
            "gayPoint": user.gayPoint,
            "profileImg": user.profileImg
        }
        returnValue.append(tmpuser)
    return JsonResponse({"response": returnValue})


"""
/api/user/createuser/<username>/<password>/<firstName>/<lastName>
Aggiunge al db un nuovo user con i dati passati
return true se l"utente è stato inserito
"""


def createUser(request, userName, psw, firstName, lastName):
    # Metodo mysql
    # user = User()
    # user.firstName = firstName
    # user.lastName = lastName
    # user.userName = userName
    # user.password = psw
    # user.description = ""
    # user.gayPoint = 0
    # user.totalPoint = 0
    # user.monthPoint = 0
    # user.profileImg = "https: // polar-tundra-64747.herokuapp.com/static/image/casadario/profile/profile-default.png"
    # try:
    #     user.save()
    # except DatabaseError:
    #     return JsonResponse({"response": False})
    # return JsonResponse({"response": True})

    # Metodo mongodb
    try:
        db = conncet()
        idCol = db["idcounter_idcollection"]
        collection = idCol.find_one()
        userCol = db["user_user"]   
        newUser = [
            {"firstName": firstName, "lastName": lastName,
                "userName": userName, "password": psw, "description": "", "gayPoint": 0,
                "totalPoint": 0, "monthPoint": 0, "profileImg": "https://polar-tundra-64747.herokuapp.com/static/image/casadario/profile/profile-default.png",
                "lastDate": "2020-01-10T23:00:00.000+00:00", "id": collection["id_user"]}
        ]
        userCol.insert_many(newUser)
    except BulkWriteError as bwe:
        return JsonResponse({"response": bwe.details["nInserted"] > 0})
    return JsonResponse({"response": True})


def getLastLogin(request, userName):
    try:
        user = User.objects.get(userName=userName)
    except (User.DoesNotExist, DatabaseError):
        return JsonResponse({"response": False})
    return JsonResponse({"response": user.lastDate})


def updateLastLogin(request, userName):
    try:
        db = conncet()
        userCol = db["user_user"]
        userCol.update_one(
            {"userName": userName}, {"$set": {"lastDate": datetime.datetime.now().isoformat()}})
    except Exception as e:
        return JsonResponse({'response': e})
    return JsonResponse({'response': True})


def updateTotalPoint(request, userName):
    try:
        db = conncet()
        user = User.objects.get(userName=userName)
        userCol = db["user_user"]
        userCol.update_one(
            {"userName": userName},
            {"$set": {"totalPoint": user.totalPoint + 1, "monthPoint": user.monthPoint + 1}})
    except BulkWriteError as bwe:
        return JsonResponse({'response': bwe.details["nInserted"] > 0})
    return JsonResponse({'response': True})

def restMonthPoint(request, userName):
    try:
        db = conncet()
        user = User.objects.get(userName=userName)
        userCol = db["user_user"]
        userCol.update_one(
            {"userName": userName}, {"$set": {"monthPoint": 0}})
    except BulkWriteError as bwe:
        return JsonResponse({'response': bwe.details["nInserted"] > 0})
    return JsonResponse({'response': True})


def getProfileImg(request, userName):
    try:
        user = User.objects.get(userName=userName)
    except (User.DoesNotExist, DatabaseError):
        return JsonResponse({"response": False})
    return JsonResponse({"response": user.profileImg})
