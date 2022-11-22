from django.urls import path
from .views import *

urlpatterns = [
    path(r'',projets,name='projet'),
    path(r'(?P<pk>[0-9]+)/$',detail_projet,name='detail_projet'),

        # projets 
    path(r'api/projets/',ProjetList.as_view(),name='projets/'),
    path(r'api/(?P<pk>[0-9]+)/$', ProjetListDetail.as_view(),name='Projetdetails/'), 
]
