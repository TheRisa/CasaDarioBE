from django.db import models

"""
DB per i tipi di oggetto
type: CharField, unique, not blank -> nome del tipo
"""


class EnterteinmentType(models.Model):
    type = models.CharField("Tipo di intrattenimento", max_length=50,
                            blank=False, unique=True)

    def __str__(self):
        return self.type


"""
DB per gli intrattenimenti
name: CharField, unique, not blank -> nome dell'intrattenimento
description: TextField -> descrizione dell'intrattenimento
type: ForeignKey a EnterteinmentType -> fk al tipo di intrattenimento
"""


class Enterteinment(models.Model):
    name = models.CharField("Nome", max_length=50,
                            blank=False, unique=True)
    description = models.TextField("Descrizione", blank=True)
    type = models.ForeignKey(
        'EnterteinmentType', on_delete=models.CASCADE, verbose_name='tipo')

    def __str__(self):
        return self.name
