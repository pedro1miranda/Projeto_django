from django import forms
from appHome.models import Usuario

class meta:
    model = Usuario
    fields = ('nome','email','senha')
    