from django.http import JsonResponse
from django.http import HttpResponse
from django.db import DatabaseError

from .models import History

"""
/api/history/
Home di api history, non fa nulla tranne render
"""


def api(request):
    return HttpResponse("Benvenuto nel back office di CasaDario, sezione History api.")
