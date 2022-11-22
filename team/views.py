from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser
from django.http import HttpResponse,HttpResponseRedirect,Http404

# Create your views here.
# Team    
# 
def team(request):
    list_teams=Team.objects.all().filter(statut=True)

    context={
            'teams':list_teams,
            }

    return render(request,"team/team.html",context)
      
class TeamList(generics.ListCreateAPIView):
    queryset=Team.objects.all().order_by('-updated')
    serializer_class=TeamSerializer
    
class TeamListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Team.objects.all()
    serializer_class=TeamSerializer  
