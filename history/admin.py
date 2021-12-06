from django.contrib import admin

from .models import History, Record


class HistoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'id']

class RecordAdmin(admin.ModelAdmin):
    list_display = ['titolo', 'user', 'descrizione', 'data']


admin.site.register(History, HistoryAdmin)
admin.site.register(Record, RecordAdmin)
