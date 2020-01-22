from django.db import models
from event import models as event_models
from user import models as user_models


class Invite(models.Model):
    event = models.IntegerField("Id evento", default=0)
    user = models.IntegerField("Id utente", default=0)
    isConfirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.event.name
