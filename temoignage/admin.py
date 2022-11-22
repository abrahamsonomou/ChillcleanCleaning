from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display=('nom','updated',)
    ordering=('nom',)
    search_field=('nom',)