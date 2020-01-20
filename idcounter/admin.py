from django.contrib import admin

from .models import IdCollection


class CounterAdmin(admin.ModelAdmin):
    list_display = ['id_user', 'id_event', 'id_invite']


admin.site.register(IdCollection, CounterAdmin)
