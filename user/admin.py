from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['userName', 'id', 'firstName', 'lastName']


admin.site.register(User, UserAdmin)
