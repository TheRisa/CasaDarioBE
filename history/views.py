from django.http import JsonResponse
from django.http import HttpResponse
from django.db import DatabaseError

from .models import History, Record
from pymongo import MongoClient

"""
/api/history/
Home di api entertainment, non fa nulla tranne render
"""

def conncet():
    myclient = MongoClient(
            "mongodb+srv://TheRisa:admin1832@casadario-kzgcj.mongodb.net/test?retryWrites=true&w=majority")
    mydb = myclient["casadario"]
    return mydb


def api(request):
    return HttpResponse("Benvenuto nel back office di CasaDario, sezione History api.")


def getAllHistory(request):
    try:
        db = conncet()
        historiesCol = db['history_history']
        histories = historiesCol.find()
    except (History.DoesNotExists, DatabaseError):
        return JsonResponse({'response': False})
    returnValue = []
    for history in histories:
        tmpHistory = {
            'name': history['name'],
            'event': history['event'],
            'date': history['date'],
            'img': history['img']
        }
        returnValue.append(tmpHistory)
    return JsonResponse({'response': returnValue})

def getRecords(request):
    try:
        db = conncet()
        recordsCol = db['history_record']
        records = recordsCol.find()
    except (History.DoesNotExists, DatabaseError):
        return JsonResponse({'response': False}) 
    returnValue = []
    for record in records:
        tmpRecord = {
            'titolo': record['titolo'],
            'user': record['user'],
            'descrizione': record['descrizione'],
            'data': record['data']
        }
        returnValue.append(tmpRecord)
    return JsonResponse({'response': returnValue})
