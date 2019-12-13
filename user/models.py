from django.db import models

# TODO: img profilo


class User(models.Model):
    userName = models.CharField(
        "User name", max_length=50, blank=False, unique=True)
    password = models.CharField("Password", max_length=50, blank=False)
    firstName = models.CharField("Nome", max_length=50, blank=False)
    lastName = models.CharField("Cognome", max_length=50, blank=False)
    totalPoint = models.IntegerField("Presenze totali", default=0)
    monthPoint = models.IntegerField("Presenze questo mese", default=0)
    gayPoint = models.IntegerField("Punti gay", default=0)
    description = models.CharField(
        "Descrizione utente", max_length=50, blank=True)
    #profileImg = models.ImageField("Immagine profilo", upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.userName
