from django.http import JsonResponse
from django.http import HttpResponse
from django.db import DatabaseError

from .models import BanList

from pymongo import MongoClient

"""
/api/banlist/
Home di api entertainment, non fa nulla tranne render
"""

def connect():
    myclient = MongoClient(
            "mongodb+srv://TheRisa:admin1832@casadario-kzgcj.mongodb.net/test?retryWrites=true&w=majority")
    mydb = myclient["casadario"]
    myCol = mydb["banlist_banlist"]
    return myCol


def api(request):
    return HttpResponse("Benvenuto nel back office di CasaDario, sezione BanList api.")


"""
/api/banlist/getlist
Rende nome e cognome di tutte le persone nella ban list
return json con tutto il db di BanList
"""


def getList(request):
    try:
        bansCol = connect()
        bans = bansCol.find()
    except DatabaseError:
        return JsonResponse({'response': ''})
    people = []
    for b in bans:
        people.append({'firstName': b['firstName'], 'lastName': b['lastName']})
    response = {'response': people}
    return JsonResponse(response)
