from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ArticleCategorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display=('nom_categorie',)
    prepopulated_fields={'slug':('nom_categorie',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('titre','auteur','categorie','created')
    list_filter=('titre','auteur',)
    prepopulated_fields={'slug':('titre',)}

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display=('auteur','updated','article',)


