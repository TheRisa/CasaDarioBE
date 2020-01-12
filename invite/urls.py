from django.urls import path

from . import views

urlpatterns = [
    path('', views.api, name='api'),
    path('addinvite/<userId>/<eventId>', views.addInvite, name='addInvite'),
    path('getinvited/<eventId>', views.getInvitedUser, name='getInvited'),
    path('getinvitedAndConfirmed/<eventId>',
         views.getInvitedAndConfirmedUser, name='getInvitedAndConfirmedUser'),
    path('confirmInvite/<confirmation>/<eventId>/<userId>',
         views.setIsConfirmed, name='setIsConfirmed'),
    path('deleteInvites/<eventId>', views.deleteOldInvites, name='deleteInvites')
]
