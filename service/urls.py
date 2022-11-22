from django.urls import path
from .views import *

urlpatterns = [
    path(r'',services,name='services'),
    path(r'(?P<pk>[0-9]+)/$',detail_service,name='detail_service'),

        # services 
    path(r'api/Services/',ServiceList.as_view(),name='Services/'),
    path(r'api/(?P<pk>[0-9]+)/$', ServiceListDetail.as_view(),name='Servicedetails/'), 
    

]
