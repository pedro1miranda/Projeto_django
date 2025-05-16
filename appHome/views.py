from django.shortcuts import render

# importe a classe HttpResponse do modulo Http dentro do pacote Django

from django.http import HttpResponse

#Função que cria a view

def appHome(request):
    return render(request, 'home.html')
