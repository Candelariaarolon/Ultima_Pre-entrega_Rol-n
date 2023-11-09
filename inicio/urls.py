from django.urls import path 
from inicio.views import inicio, usuarios



urlpatterns = [
    path('inicio/', inicio),
    path ('usuarios/', usuarios)
    
]


