from django.http import HttpResponse

from .models import Event

# TODO: tipo tutto


def api(request):
    return HttpResponse("Benvenuto nel back office di CasaDario, sezione Event api.")
