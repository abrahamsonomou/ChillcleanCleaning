from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser
from service.models import *
from temoignage.models import *
from blog.models import *
from team.models import *
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)
  
# Create your views here.
def index(request):
    recent_articles=Article.objects.filter(statut=True).order_by('-updated')[:3]
    list_services=Service.objects.all().filter(statut=True)
    list_temoignages=Temoignage.objects.all().filter(statut=True)
    list_teams=Team.objects.all().filter(statut=True)

    context={
            'services':list_services,
            'temoignages':list_temoignages,
            'teams':list_teams,
            'recent_articles':recent_articles,
            }
    

    return render(request,"pages/index.html",context)

def shop(request):
    return render(request,"pages/shop.html")

def about(request):
    return render(request,"pages/about.html")

def projet(request):
    return render(request,"pages/projet.html")




  

