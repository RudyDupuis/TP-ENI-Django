from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('recette/<int:id>/', views.recette)
]