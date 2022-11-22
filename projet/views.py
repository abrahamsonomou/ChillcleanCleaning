from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser
from django.http import HttpResponse,HttpResponseRedirect,Http404

# liste des Projets
def projets(request):
    projets=Projet.objects.filter(statut=True)
    context={
        'projets':projets,
        }
    return render(request,"projets/projet.html",context)

# detail d'un Projet
def detail_projet(request,pk:int):
    try:
        projet=Projet.objects.get(pk=pk)
        projets=Projet.objects.filter(statut=True)

        context={
            'projet':projet,
            'projets':projets,
        }
    except Projet.DoesNotExist:
        raise('This Projet doesnot exist')
    return render(request,'projets/detail_projet.html',context)


# Projets 
class ProjetList(generics.ListCreateAPIView):
    queryset=Projet.objects.all().order_by('-updated')
    serializer_class=ProjetSerializer
    
class ProjetListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Projet.objects.all()
    serializer_class=ProjetSerializer 