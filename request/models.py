from django.db import models


"""
DB per le richieste ricevute da FE per l'admin
title: CharField, unique, not blank -> titolo della richiesta
body: TextField, not blank -> body della richiesta
data: DateField -> data della richiesta, impostata automaticamente alla creazione della richiesta
"""


class Requests(models.Model):
    title = models.CharField("Nome dell'evento",
                             max_length=50, blank=False, unique=True)
    body = models.TextField("Descrizione dell'evento", blank=False)
    date = models.DateField(auto_now=True, blank=False)

    def __str__(self):
        return self.title
