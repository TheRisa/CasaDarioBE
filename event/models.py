from django.db import models

# TODO: array di persone partecipanti e di compiti (guarda se puoi usare json come field)


class Event(models.Model):
    name = models.CharField("Nome evento", max_length=50, blank=False)
    description = models.TextField("Descrizione evento", blank=True)
    place = models.CharField("Luogo", max_length=100, blank=False)
    date = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    initHour = models.TimeField(
        "Ora di inizio", auto_now=False, auto_now_add=False, blank=True)
    endHour = models.TimeField(
        "Ora di fine", auto_now=False, auto_now_add=False, blank=True)

    def __str__(self):
        return self.name
