from django.db import models

"""
DB per memorizzare le richieste per l'app
title: CharField, not blank -> titolo richiesta
todo: CharField, not blank -> body della richiesta
"""


class Todo(models.Model):
    title = models.CharField("Titolo", max_length=50, blank=False)
    todo = models.TextField("To do", blank=False)

    def __str__(self):
        return self.title
