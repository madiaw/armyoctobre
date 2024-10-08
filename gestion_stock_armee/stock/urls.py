from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
    path('article/<int:pk>/', views.detail_article, name='detail_article'),
    path('article/ajouter/', views.ajouter_article, name='ajouter_article'),
    path('article/<int:pk>/modifier/', views.modifier_article, name='modifier_article'),
    path('mouvement/ajouter/', views.ajouter_mouvement, name='ajouter_mouvement'),
]