from django.http import JsonResponse
from django.http import HttpResponse
from django.db import DatabaseError


from pymongo import MongoClient

from .models import Todo

"""
/api/askme/
Home di api entertainment, non fa nulla tranne render
"""


def api(request):
    return HttpResponse("Benvenuto nel back office di CasaDario, sezione Askme api.")


"""
/api/askme/addTodo
Aggiunge un todo al db
return json con boolean flag per la chiamata riuscita
"""


def addTodo(request, title, body):
    # todo = Todo()
    # todo.title = title
    # todo.todo = body
    # try:
    #     todo.save()
    # except DatabaseError:
    #     return JsonResponse({'response': False})
    # return JsonResponse({'response': True})

    myclient = MongoClient(
        "mongodb+srv://TheRisa:admin1832@casadario-kzgcj.mongodb.net/test?retryWrites=true&w=majoritys")
    mydb = myclient["casadario"]
    mycol = mydb["askme_todo"]

    mylist = [
        {"name": "Amy", "address": "Apple st 652"},
        {"name": "Hannah", "address": "Mountain 21"},
        {"name": "Michael", "address": "Valley 345"}
    ]

    mycol.insert_many(mylist)
