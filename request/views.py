from django.http import JsonResponse
from django.http import HttpResponse
from django.db import DatabaseError

from .models import Requests

"""
/api/requests/
Home di api requests, non fa nulla tranne render
"""


def api(request):
    return HttpResponse("Benvenuto nel back office di CasaDario, sezione Requests api.")
