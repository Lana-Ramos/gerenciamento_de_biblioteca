from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def acervo(request):
    return HttpResponse('Bem-vindo ao Acervo da Biblioteca!')