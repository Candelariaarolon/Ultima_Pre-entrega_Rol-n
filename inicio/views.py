from django.shortcuts import render
from inicio.models import Usuarios

# Create your views here.

def inicio(request):
    
    return render(request, 'inicio/inicio.html', {})
    
   # template = loader.get_template('inicio.html')
   # template_renderizado = template.render({})
   # return HttpResponse(template_renderizado)
   
def usuarios(request):
    usuario = Usuarios(nombre='Candelaria', apellido= 'Rolon', edad= 18)
    usuario.save()
    
    return render(request, 'inicio/usuarios.html', {'usuario': usuario})
    