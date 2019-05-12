from django.http import JsonResponse
from django.http import HttpResponse
from django.db import DatabaseError

from .models import Enterteinment
from .models import EnterteinmentType

"""
/api/user/
Home di api entertainment, non fa nulla tranne render
"""


def api(request):
    return HttpResponse("Benvenuto nel back office di CasaDario, sezione Entertainment api.")


"""
/api/entertainment/getentertainmentbytype/<type>/
Fa ricerca su db per trovare tutti i giochi del type specificato
return json con intrattenimenti di tipo type
"""


def getEntertainmentByType(request, type):
    try:
        typeName = EnterteinmentType.objects.get(type=type)
        entertainment = Enterteinment.objects.filter(type=typeName)
    except (Enterteinment.DoesNotExist, EnterteinmentType.DoesNotExist, DatabaseError):
        return JsonResponse({'response': ''})
    listOfGame = []
    for ent in entertainment:
        game = {'name': ent.name,
                'description': ent.description,
                }
        listOfGame.append(game)
    response = {'response': listOfGame}
    return JsonResponse(response)


"""
/api/entertainment/getentertainmenttypes/
Torna tutti gli oggetti di EntertainmentType DB
return json con tutti i tipi di intrattenimento
"""


def getEntertainmentTypes(request):
    try:
        types = EnterteinmentType.objects.all()
    except DatabaseError:
        return JsonResponse({'response': ''})
    listOfTypes = []
    for t in types:
        listOfTypes.append(t.type)
    response = {'response': listOfTypes}
    return JsonResponse(response)


"""
/api/entertainment/getentertainmentbyname/<name>/
Rende l'intrattenimento col nome name
return json con nome descrizione e tipo dell'intrattenimento <name>
"""


def getEntertainmentByName(request, name):
    try:
        entertainment = Enterteinment.objects.get(name=name)
        typeName = EnterteinmentType.objects.get(type=entertainment.type)
    except (Enterteinment.DoesNotExist, EnterteinmentType.DoesNotExist, DatabaseError):
        return JsonResponse({'response': ''})
    response = {'response': {
        'name': entertainment.name,
        'type': typeName.type,
        'description': entertainment.description
    }}
    return JsonResponse(response)
