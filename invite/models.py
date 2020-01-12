from django.db import models
from event import models as event_models
from user import models as user_models


class Invite(models.Model):
    event = models.ForeignKey(
        event_models.Event, on_delete=models.CASCADE, verbose_name='event')
    user = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE, verbose_name='user')
    isConfirmed = models.BooleanField(balnk=True, default=False)

    def __str__(self):
        return self.event.name
