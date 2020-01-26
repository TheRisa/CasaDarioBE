from django.urls import path

from . import views

urlpatterns = [
    path('', views.api, name='api'),
    path('getEvents/<userNameInput>', views.getAllUserEvents, name='getAllUserEvents'),
    path('getAllEvents', views.getAllEvents, name='getAllEvents'),
    path('deleteOldEvent/<eventId>', views.deleteOldEvent, name='deleteOldEvent'),
    path('createEvent', views.createEvent, name='createEvent'),
    path('updateEvent/<eventId>', views.updateEvent, name='updateEvent')
]
