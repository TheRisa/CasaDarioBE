from django.contrib import admin

from .models import History


class HistoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'id']


admin.site.register(History, HistoryAdmin)
