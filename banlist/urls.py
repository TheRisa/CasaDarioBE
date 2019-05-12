from django.urls import path

from . import views

urlpatterns = [
    path('', views.api, name='api'),
    path('getlist', views.getList, name='getList')
]
