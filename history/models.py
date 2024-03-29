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
    img = models.TextField(
        "Url immagine", blank=True, default="https://polar-tundra-64747.herokuapp.com/static/image/casadario/history/history-default.png")

    def __str__(self):
        return self.name

"""
Modello per i record
"""

class Record(models.Model):
    titolo = models.CharField("Titolo del record",
                            max_length=100, blank=False, unique=True)
    user = models.CharField("Nome della storia",
                            max_length=50, blank=False, unique=True)
    descrizione = models.CharField("Nome della storia",
                            max_length=50, blank=False, unique=True)
    data = models.CharField("Nome della storia",
                            max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.titolo
