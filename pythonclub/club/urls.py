from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index' ),
path('resources/', views.resources, name='resources'),
path('getmeetings/', views.getmeetings, name='getmeetings'),
path('meetingdetail/<int:id>', views.meetingdetail, name='details'), #the int id part includes the id in the url
path('addmeeting/', views.addMeeting, name='addmeeting' ),
path('loginmessage/', views.loginmessage, name='loginmessage'),
path('logoutmessage/', views.logoutmessage, name='logoutmessage')
]