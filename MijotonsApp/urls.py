from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('recette/<int:id>/', views.recette),
    path('recette/ajouter/', views.ajouter),
    path('recette/<int:id>/supprimer/', views.supprimer),
    path('recette/<int:id>/modifier/', views.modifier),
]