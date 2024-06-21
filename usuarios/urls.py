from django.urls import path 
from usuarios.views import registrar_usuario, agregar_producto, pagina_principal

urlpatterns = [
    path('registro/', registrar_usuario, name='registro_usuario'),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('pagina-principal/', pagina_principal, name='pagina_principal')
    
    
]
