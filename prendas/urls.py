from django.urls import path 
from prendas.views import prendas, agregoprendas, prendas_css

urlpatterns = [
    
    path('', prendas, name='prendas'),
    path('agregoprendas/', agregoprendas),
    path('css/prendas.css/', prendas_css, name='prendas_css'),
]

