from django.http import JsonResponse
from django.http import HttpResponse
from django.db import DatabaseError

from .models import History

"""
/api/history/
Home di api entertainment, non fa nulla tranne render
"""


def api(request):
    return HttpResponse("Benvenuto nel back office di CasaDario, sezione History api.")


def getAllHistory(request):
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
