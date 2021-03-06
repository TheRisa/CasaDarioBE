from django.http import JsonResponse
from django.http import HttpResponse
from django.db import DatabaseError

from pymongo.errors import BulkWriteError
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
    # Metodo per mysql
    # todo = Todo()
    # todo.title = title
    # todo.todo = body
    # try:
    #     todo.save()
    # except DatabaseError:
    #     return JsonResponse({'response': False})
    # return JsonResponse({'response': True})

    # Metodo per mongodb
    try:
        myclient = MongoClient(
            "mongodb+srv://TheRisa:admin1832@casadario-kzgcj.mongodb.net/test?retryWrites=true&w=majority")
        mydb = myclient["casadario"]
        mycol = mydb["askme_todo"]
        mylist = [
            {"title": title, "todo": body}
        ]
        mycol.insert_many(mylist)
    except BulkWriteError:
        return JsonResponse({'response': False})
    return JsonResponse({'response': True})
