from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)
    
# Create your views here.
def blog(request):
    recent_articles=Article.objects.filter(statut=True).order_by('-updated')[:5]
    list_articles=Article.objects.all().filter(statut=True)
    list_categorie=ArticleCategorie.objects.all()
    
    paginator=Paginator(list_articles,2)
    page=request.GET.get('page')
    try:
        articles=paginator.page(page)
    except PageNotAnInteger:
        articles=paginator.page(1)
    except EmptyPage:
        articles=paginator.page(paginator.num_pages)
    
    context={
            'articles':articles,
            'categories':list_categorie,
            'page':page,
            'recent_articles':recent_articles,
            }
    return render(request,"blog/blog.html",context)

def detail_article(request,pk:int):
    try:
        article=Article.objects.get(pk=pk)
        categorie=article.categorie
        list_categorie=ArticleCategorie.objects.all()
        article_en_relation=Article.objects.filter(categorie=categorie)[:5]
        context={
            'article_en_relation':article_en_relation,
            'article':article,
            'categories':list_categorie,
        }
    except Article.DoesNotExist:
        raise('This article doesnot exist')
    return render(request,'blog/detail_article.html',context)

def search_article(request):
    query=request.GET["article"]
    list_categorie=ArticleCategorie.objects.all()
    object_list=Article.objects.filter(statut=True).filter(titre__icontains=query)
    paginator=Paginator(object_list,4)
    recent_articles=Article.objects.filter(statut=True).order_by('-updated')[:5]

    page=request.GET.get('page')
    try:
        liste_article=paginator.page(page)
    except PageNotAnInteger:
        liste_article=paginator.page(1)
    except EmptyPage:
        liste_article=paginator.page(paginator.num_pages)
    
    context={
            'articles':liste_article,
            'page':page,
            'categories':list_categorie,
            'recent_articles':recent_articles,
            }
    return render(request,'blog/search_article.html',context)

# selection des articles par categorie
def selection_article_categorie(request,categorie:str):
    list_categorie=ArticleCategorie.objects.all()
    object_list=Article.objects.filter(statut=True).filter(categorie=categorie)
    paginator=Paginator(object_list,4)
    recent_articles=Article.objects.filter(statut=True).order_by('-updated')[:5]

    page=request.GET.get('page')
    try:
        liste_article=paginator.page(page)
    except PageNotAnInteger:
        liste_article=paginator.page(1)
    except EmptyPage:
        liste_article=paginator.page(paginator.num_pages)
    
    context={
            'articles':liste_article,
            'page':page,
            'categories':list_categorie,
            'recent_articles':recent_articles,
            }
    return render(request,'blog/selection_article_categorie.html',context)



# la class ArticleCategorie 
class ArticleCategorieList(generics.ListCreateAPIView):
    queryset=ArticleCategorie.objects.all()
    serializer_class=ArticleCategorieSerializer
    permission_classes = [IsAdminUser]
    
class ArticleCategorieListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=ArticleCategorie.objects.all()
    serializer_class=ArticleCategorieSerializer    
    permission_classes = [IsAdminUser]

# la class Article
class ArticleList(generics.ListCreateAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    permission_classes = [IsAdminUser]
    
class ArticleListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer    
    permission_classes = [IsAdminUser]
 
# la class Commentaire
class CommentaireList(generics.ListCreateAPIView):
    queryset=Commentaire.objects.all()
    serializer_class=CommentaireSerializer
    permission_classes = [IsAdminUser]
    
class CommentaireListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Commentaire.objects.all()
    serializer_class=CommentaireSerializer    
    permission_classes = [IsAdminUser]
    
