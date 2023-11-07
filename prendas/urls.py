from django.urls import path 
from prendas.views import prendas, PrendasRopa


urlpatterns = [
    path('', prendas),
    path('prendasropa/', PrendasRopa)
]