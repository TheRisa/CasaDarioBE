from django.contrib import admin
from .models import Curiosity


class CuriosityAdmin(admin.ModelAdmin):
    list_display = ['curiosityText', 'id']


admin.site.register(Curiosity, CuriosityAdmin)
