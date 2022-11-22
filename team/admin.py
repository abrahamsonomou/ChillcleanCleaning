from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=('nom','fonction','updated')
    ordering=('nom',)