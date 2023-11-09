from django.urls import path 
from pago.views import pago, agregopago


urlpatterns = [
    path('', pago),
    path('agregopago/', agregopago)
]