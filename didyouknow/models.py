from django.db import models


class Curiosity(models.Model):
    curiosityText = models.TextField(
        "Curiosity text", blank=False, max_length=200, unique=True)

    def __str__(self):
        return self.curiosityText
