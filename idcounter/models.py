from django.db import models


class IdCollection(models.Model):
    collection_id = models.IntegerField("Id per il get", default=1)
    id_user = models.IntegerField("Max id utenti", default=0)
    id_invite = models.IntegerField("Max id inviti", default=0)
    id_event = models.IntegerField("Max id eventi", default=0)
