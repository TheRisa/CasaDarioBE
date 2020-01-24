from django.http import HttpResponse
from django.http import JsonResponse

import random
import json

from .models import Curiosity

"""
/api/didyouknow/
Home di api did you know
return json con testo di una curiosità a caso
"""

def connect():
    myclient = MongoClient(
            "mongodb+srv://TheRisa:admin1832@casadario-kzgcj.mongodb.net/test?retryWrites=true&w=majority")
    mydb = myclient["casadario"]
    myCol = mydb["didyouknow_curiosity"]
    return myCol


def api(request):
    try:
        curiosityCol = connect()
        curiosity = curiosityCol.aggregate([{ "$sample": { "size": 1 } }])
    except DatabaseError:
        return JsonResponse({'response': False})
    return JsonResponse({"response": curiosity['curiosityText']})
