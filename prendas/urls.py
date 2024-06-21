from django.urls import path 
from prendas.views import prendas_css, subir_prenda, prendas, nuevos_ingresos, guardar_comentario
urlpatterns = [
    
    path('', prendas, name='prendas'),
    path('css/prendas.css/', prendas_css, name='prendas_css'),
    path('subir-prenda/', subir_prenda, name='subir_prenda'),
    path('nuevos-ingresos/', nuevos_ingresos, name='nuevos_ingresos'),
        path('guardar-comentario/<int:prenda_id>/', guardar_comentario, name='guardar_comentario'),
]

