from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def emprestimos(request):
    return HttpResponse("Bem-vindo à seção de Empréstimos da Biblioteca!")
