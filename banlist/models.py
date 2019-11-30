from django.db import models

"""
DB per memorizzare la gente bannata
firstName: CharField, not blank -> nome
lastName: CharField, not blank -> cognome
"""


class BanList(models.Model):
    firstName = models.CharField("Nome", max_length=50, blank=False)
    lastName = models.CharField("Cognome", max_length=50, blank=False)

    def __str__(self):
        return self.firstName + ' ' + self.lastName
