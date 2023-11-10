from django.urls import path 
from inicio.views import inicio, usuarios



urlpatterns = [
    path('', inicio),
    path ('usuarios/', usuarios)
    
]


