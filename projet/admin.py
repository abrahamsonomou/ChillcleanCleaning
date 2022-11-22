from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ProjetCategorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display=('nom_categorie',)
    prepopulated_fields={'slug':('nom_categorie',)}


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display=('titre','categorie','client','location','architect','value','annee','created')
    list_filter=('titre','categorie',)