from django.urls import path

from . import views

urlpatterns = [
    path('', views.api, name='api'),
    path('login/<userName>/<psw>', views.logIn, name='logIn'),
    path('getUser/<userName>/', views.getUser, name='getUser'),
    path('getAllUsers/', views.getAllUsers, name='getAllUser'),
    path('getLastLogin/<userName>', views.getLastLogin, name='getLastLogin'),
    path('getProfileImg/<userName>', views.getProfileImg, name='getProfileImg'),
    path('getAchivments/<userName>', views.getAchivments, name='getAchivments'),
    path('updateAchievements/<userName>/<total>/<achievements>', views.updateAchievements, name='updateAchievements'),
    path('updateLastLogin/<userName>', views.updateLastLogin, name='updateLastLogin'),
    path('addGayPoint/<userName>', views.addGayPoint, name='addGayPoint'),
    path('addNapoliPoint/<userName>', views.addNapoliPoint, name='addNapoliPoint'),
    path('updateTotalPoint/<userName>', views.updateTotalPoint, name='updateTotalPoint'),
    path('addNewYear/<userName>', views.addNewYear, name='addNewYear'),
    path('updatePlayerId/<userName>/<playerId>', views.updatePlayerId, name='updatePlayerId'),
    path('resetMonthPoint/', views.restMonthPoint, name='resetMonthPoint'),
    path('createuser/<userName>/<psw>/<firstName>/<lastName>/', views.createUser, name='createUser')
]
