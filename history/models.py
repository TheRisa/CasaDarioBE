from django.db import models


"""
DB per le storie di casaDario
name: CharField, unique, not blank -> titolo della storia
event: TextField, not blank -> descrizione della storia
date: DateField -> data della storia
"""


class History(models.Model):
    name = models.CharField("Nome dell'evento",
                            max_length=50, blank=False, unique=True)
    event = models.TextField("Descrizione dell'evento", blank=False)
    date = models.DateField("Data", auto_now=False,
                            auto_now_add=False, blank=True)

    def __str__(self):
        return self.name
