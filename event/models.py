from django.db import models
from user import models as user_models


class Event(models.Model):
    name = models.CharField("Nome evento", max_length=50, blank=False)
    description = models.TextField("Descrizione evento", blank=True)
    place = models.CharField("Luogo", max_length=100, blank=False)
    date = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    initHour = models.TimeField(
        "Ora di inizio", auto_now=False, auto_now_add=False, blank=True)
    type = models.TextField("Tipo di evento", blank=True)
    creator = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE, verbose_name='Creatore evento')

    def __str__(self):
        return self.name
