from django.urls import path
from . import views

urlpatterns = [
    path('', views.emprestimos, name='emprestimos'),
]