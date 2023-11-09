from django.shortcuts import render

from prendas.models import PrendasRopa
# Create your views here.

def prendas(request):
    prendas = PrendasRopa.objects.all()
    return render(request, 'prendas/prendas.html', {'prendas': prendas})

def agregoprendas(request):
    botas = PrendasRopa (marca='Sarkany', talle='37', descripcion='Botas texanas. Como nuevas.', temporada= 2023)
    botas.save()
    
    return render(request, 'prendas/prendas.html', {'botas': botas})