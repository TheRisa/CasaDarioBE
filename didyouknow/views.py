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


def api(request):
    try:
        curiosity = Curiosity.objects.all()
    except DatabaseError:
        return JsonResponse({'response': ''})
    response = {'response': curiosity[random.randint(
        0, curiosity.count() - 1)].curiosityText}
    return JsonResponse(response)
