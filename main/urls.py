from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index,name='index'),

    # l'application contact
    path('contact/',include('contact.urls')),
    path('services/',include('service.urls')),
    path('team/',include('team.urls')),
    path('temoignage/',include('temoignage.urls')),
    path('blog/',include('blog.urls')),
    path('projet/',include('projet.urls')),

    path('about',about,name='about'),
    path('shop',shop,name='shop'),
]
