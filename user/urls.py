from django.urls import path

from . import views

urlpatterns = [
    path('', views.api, name='api'),
    path('login/<userName>/<psw>', views.logIn, name='logIn'),
    path('getUser/<userName>/', views.getUser, name='getUser'),
    path('getAllUsers/', views.getAllUsers, name='getAllUser'),
    path('getLastLogin/<userName>', views.getLastLogin, name='getLastLogin'),
    path('getProfileImg/<userName>', views.getProfileImg, name='getProfileImg'),
    path('updateLastLogin/<userName>',
         views.updateLastLogin, name='updateLastLogin'),
    path('updateTotalPoint/<userName>',
         views.updateTotalPoint, name='updateTotalPoint'),
    path('resetMonthPointt/<userName>',
         views.restMonthPoint, name='resetMonthPoint'),
    path('createuser/<userName>/<psw>/<firstName>/<lastName>/',
         views.createUser, name='createUser')
]
