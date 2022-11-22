from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

    # services 
class ServiceSerializer(ModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model=Service
        fields=['nom','description','image'] 
 