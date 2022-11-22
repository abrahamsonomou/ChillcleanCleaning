from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

#serialisation de la classe Contact
class ContactSerializer(ModelSerializer):
    class Meta:
        model=Contact
        fields=['nom','email','sujet','message'] 

    # NewLetter
class NewsLetterSerializer(ModelSerializer):
    class Meta:
        model=NewsLetter
        fields=['email'] 