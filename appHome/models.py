from django.db import models

# Create your models here.

class Usuario():
    nome = models.CharField(max_length = 255)
    sobrenome = models.CharField(max_length = 255)

class Login(models.Model):
    nomeUsuario = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    senha = models.IntegerField()
    
    