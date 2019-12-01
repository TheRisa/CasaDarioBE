from django.contrib import admin
from .models import Invite


class InviteAdmin(admin.ModelAdmin):
    list_display = ['event', 'user']


admin.site.register(Invite, InviteAdmin)
