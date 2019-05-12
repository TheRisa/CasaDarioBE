from django.contrib import admin

from .models import BanList


class BanListAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'id']


admin.site.register(BanList, BanListAdmin)
