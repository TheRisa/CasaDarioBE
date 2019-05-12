from django.contrib import admin


from .models import Requests


class RequestsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'id']


admin.site.register(Requests, RequestsAdmin)
