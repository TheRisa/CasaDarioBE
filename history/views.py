from django.http import JsonResponse
from django.http import HttpResponse
from django.db import DatabaseError

from .models import History, Record

"""
/api/history/
Home di api entertainment, non fa nulla tranne render
"""


def api():
    return HttpResponse("Benvenuto nel back office di CasaDario, sezione History api.")


def getAllHistory():
    try:
        histories = History.objects.all()
    except (History.DoesNotExists, DatabaseError):
        return JsonResponse({'response': False})
    returnValue = []
    for history in histories:
        tmpHistory = {
            'name': history.name,
            'event': history.event,
            'date': history.date,
            'img': history.img
        }
        returnValue.append(tmpHistory)
    return JsonResponse({'response': returnValue})

def getRecords():
    try:
        records = Record.objects.all()
    except (History.DoesNotExists, DatabaseError):
        return JsonResponse({'response': False}) 
    returnValue = []
    for record in records:
        tmpRecord = {
            'titolo': record.titolo,
            'user': record.user,
            'descrizione': record.descrizione,
            'data': record.data
        }
        returnValue.append(tmpRecord)
    return JsonResponse({'response': returnValue})
