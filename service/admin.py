from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=('titre','slug','created',)
    list_filter=('titre',)
    prepopulated_fields={'slug':('titre',)}