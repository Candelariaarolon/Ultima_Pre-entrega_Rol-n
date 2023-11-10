from django.urls import path 
from inicio.views import inicio, usuarios



urlpatterns = [
    path('', inicio, name='inicio'),
    path ('usuarios/', usuarios, name= 'usuarios')
    
]


