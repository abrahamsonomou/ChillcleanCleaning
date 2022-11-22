from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

    # Temoignage       
class TemoignageSerializer(ModelSerializer):
    photo = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model=Temoignage
        fields=['nom','contenu','photo'] 
        