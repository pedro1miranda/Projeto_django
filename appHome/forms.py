from django import forms
from appHome.models import Usuario, Login

class meta:
    model = Usuario
    fields = ('nome','sobrenome')

class meta: model