#importa a função .path no modulo django.urls
from django.urls import path;

#Importa o modulo views no diretorio atual;
from . import views;

#lista de objetos path, define padrões urls

urlpatterns = [
    path('', views.appHome, name="appHome"),
]

