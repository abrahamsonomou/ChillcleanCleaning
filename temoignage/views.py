from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser
from django.http import HttpResponse,HttpResponseRedirect,Http404

def temoignage(request):
    return render(request,"pages/temoignage.html")

# rest_framwork
# Temoignage       
class TemoignageList(generics.ListCreateAPIView):
    queryset=Temoignage.objects.all().order_by('-updated')
    serializer_class=TemoignageSerializer
    
class TemoignageListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Temoignage.objects.all()
    serializer_class=TemoignageSerializer  
  