from django.http import JsonResponse
from django.http import HttpResponse
from django.db import DatabaseError

from .models import BanList

"""
/api/banlist/
Home di api entertainment, non fa nulla tranne render
"""


def api(request):
    return HttpResponse("Benvenuto nel back office di CasaDario, sezione BanList api.")


"""
/api/banlist/getlist
Rende nome e cognome di tutte le persone nella ban list
return json con tutto il db di BanList
"""


def getList(request):
    try:
        bans = BanList.objects.all()
    except DatabaseError:
        return JsonResponse({'response': ''})
    people = []
    for b in bans:
        people.append({'firstName': b.firstName, 'lastName': b.lastName})
    response = {'response': people}
    return JsonResponse(response)
