from django.urls import path

from . import views

urlpatterns = [
    path('', views.api, name='api'),
    path('getentertainmentbytype/<type>/',
         views.getEntertainmentByType, name='getEntertainmentByType'),
    path('getentertainmenttypes/',
         views.getEntertainmentTypes, name='getEntertainmentTypes'),
    path('getentertainmentbyname/<name>',
         views.getEntertainmentByName, name='getEntertainmentByName'),
]
