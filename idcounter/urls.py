from django.urls import path

from . import views

urlpatterns = [
    path('getUser', views.getUser, name='getUser'),
    path('getEvent', views.getEvent, name='getEvent'),
    path('getInvite', views.getInvite, name='getInvite')
]
