from django.urls import path

from . import views

urlpatterns = [
    path('', views.api, name='api'),
    path('getAllHistories', views.getAllHistory, name='getAllHistory'),
    path('getRecords', views.getRecords, name='getRecords')
]
