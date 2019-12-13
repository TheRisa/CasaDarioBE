from django.urls import path

from . import views

urlpatterns = [
    path('', views.api, name='api'),
    path('getEvents/<userNameInput>', views.getAllEvents, name='getAllEvents'),
    path('createEvent', views.createEvent, name='createEvent')
]
