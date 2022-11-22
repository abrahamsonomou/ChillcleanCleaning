from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser
from django.http import HttpResponse,HttpResponseRedirect,Http404

# liste des services
def services(request):
    services=Service.objects.filter(statut=True)
    context={
        'services':services,
        }
    return render(request,"services/services.html",context)

# detail d'un service
def detail_service(request,pk:int):
    try:
        service=Service.objects.get(pk=pk)
        services=Service.objects.filter(statut=True)

        context={
            'service':service,
            'services':services,
        }
    except service.DoesNotExist:
        raise('This service doesnot exist')
    return render(request,'services/detail_service.html',context)


# services 
class ServiceList(generics.ListCreateAPIView):
    queryset=Service.objects.all().order_by('-updated')
    serializer_class=ServiceSerializer
    
class ServiceListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Service.objects.all()
    serializer_class=ServiceSerializer 