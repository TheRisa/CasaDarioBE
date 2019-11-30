from django.urls import path

from . import views

urlpatterns = [
    path('', views.api, name='api'),
    path('addTodo/<title>/<body>', views.addTodo, name='addTodo')
]
