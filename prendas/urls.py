from django.urls import path 
from prendas.views import prendas, agregoprendas, PrendasRopa


urlpatterns = [
    
    path('', prendas, name='prendas'),
    path('agregoprendas/', agregoprendas)
]