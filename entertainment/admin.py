from django.contrib import admin

from .models import Enterteinment
from .models import EnterteinmentType


class EntertainmentTypeAdmin(admin.ModelAdmin):
    list_display = ['type', 'id']


class EntertainmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'type']


admin.site.register(Enterteinment, EntertainmentAdmin)
admin.site.register(EnterteinmentType, EntertainmentTypeAdmin)
