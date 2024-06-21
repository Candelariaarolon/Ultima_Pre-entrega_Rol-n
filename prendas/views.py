from django.shortcuts import render
from django.http import HttpResponse

from prendas.models import PrendasRopa
# Create your views here.

def prendas(request):
    prendas = PrendasRopa.objects.all()
    return render(request, 'prendas/prendas.html', {'prendas': prendas})

def agregoprendas(request):
    botas = PrendasRopa (marca='Sarkany', talle='37', descripcion='Botas texanas. Como nuevas.', temporada= 2023)
    botas.save()
    
    return render(request, 'prendas/prendas.html', {'botas': botas})


def prendas_css(request):
    # puedo cargar el archivo CSS y devolverlo como respuesta
    with open('prendas/prendas.css', 'r') as f:
        css_content = f.read()
    return HttpResponse(css_content, content_type='text/css')