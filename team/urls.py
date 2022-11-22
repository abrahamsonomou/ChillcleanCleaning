from django.urls import path
from .views import *

urlpatterns = [
    path('',team,name='team'),

   # Team      
    path(r'api/teams/',TeamList.as_view(),name='teams/'),
    path(r'api/(?P<pk>[0-9]+)/$', TeamListDetail.as_view(),name='teamdetails/'), 

]
