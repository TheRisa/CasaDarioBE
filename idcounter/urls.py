from django.urls import path

from . import views

urlpatterns = [
    path('getUser', views.getUser, name='getUser'),
    path('incrementUser', views.incrementUser, name='incrementUser'),
    path('getEvent', views.getEvent, name='getEvent'),
    path('incrementEvent', views.incrementEvent, name='incrementEvent'),
    path('getInvite', views.getInvite, name='getInvite'),
    path('incrementInvite', views.incrementInvite, name='incrementInvite')
]
