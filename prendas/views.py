from django.shortcuts import render, redirect
from django.http import HttpResponse
from prendas.models import PrendasRopa
from .forms import PrendaForm

# Create your views here.


def prendas(request):
    prendas = PrendasRopa.objects.all()
    return render(request, 'prendas/prendas.html', {'prendas': prendas})


def prendas_css(request):
    # puedo cargar el archivo CSS y devolverlo como respuesta
    with open('prendas/prendas.css', 'r') as f:
        css_content = f.read()
    return HttpResponse(css_content, content_type='text/css')


def subir_prenda(request):
    if request.method == 'POST':
        form = PrendaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('nuevos_ingresos')
    else:
        form = PrendaForm()
    return render(request, 'prendas/subirprendas.html', {'form': form})

def nuevos_ingresos(request):
    nuevas_prendas = PrendasRopa.objects.all().order_by('-Fecha')[:10]  
    return render(request, 'prendas/nuevosingresos.html', {'nuevas_prendas': nuevas_prendas})