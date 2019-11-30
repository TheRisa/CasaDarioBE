from django.db import models


"""
DB per i tipi di oggetto
type: CharField, unique, not blank -> nome del tipo
"""


class History(models.Model):
    name = models.CharField("Nome della storia",
                            max_length=50, blank=False, unique=True)
    event = models.TextField("Descrizione della storia", blank=False)
    date = models.DateField(auto_now=False, auto_now_add=False, blank=True)

    def __str__(self):
        return self.name
