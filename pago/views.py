from django.shortcuts import render
from pago.models import Pago

def pago(request):
    return render(request, 'pago/pago.html', {})

def agregopago(request):
    pago = Pago (user='Cande', medio_pago='debito', numero_tarjeta='781230987600', codigo_seguridad=654)
    pago.save()
    return render(request, 'pago/pago.html', {'pago': pago})
