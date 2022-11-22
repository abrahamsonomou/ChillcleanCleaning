from django.db import models
import uuid
from django.template.defaultfilters import slugify
from django.urls import reverse
from django_quill.fields import QuillField
from django.conf import settings

# Create your models here.

CustomUser=settings.AUTH_USER_MODEL 

class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')

    class Meta:
        abstract=True