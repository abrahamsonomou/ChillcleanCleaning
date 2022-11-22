from django.urls import path
from .views import *

urlpatterns = [
    path(r'',blog,name='blog'),
    path(r'(?P<pk>[0-9]+)/$',detail_article,name='detail_article'),
    path('<categorie>/',selection_article_categorie,name='selection_article_categorie'),
    path(r'article/recherche',search_article,name='search_article'),
    
    # la class ArticleCategorie 
    path(r'api/ArticleCategories/',ArticleCategorieList.as_view(),name='ArticleCategories/'),
    path(r'api/(?P<pk>[0-9]+)/$', ArticleCategorieListDetail.as_view(),name='ArticleCategoriedetails/'),
    
    # la class Article
    path(r'api/Articles/',ArticleList.as_view(),name='Article/'),
    path(r'api/(?P<pk>[0-9]+)/$', ArticleListDetail.as_view(),name='Articledetails/'),
    
    # la class Commentaire
    path(r'api/Commentaires/',CommentaireList.as_view(),name='Commentaires/'),
    path(r'api/(?P<pk>[0-9]+)/$', CommentaireListDetail.as_view(),name='Commentairedetails/'),
    
]
