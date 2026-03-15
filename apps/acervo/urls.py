from django.urls import path
from .views import acervo

urlpatterns = [
    path('', acervo, name='acervo'),
]