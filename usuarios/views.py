from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login 
from .models import Usuario
from django import forms
from .forms import LoginForm

class RegistroUsuarioForm(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'apellido', 'contrasena', 'tipo_usuario']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["contrasena"])
        if commit:
            user.save()
        return user
    
    
def agregar_producto(request):
    
    return HttpResponse("Agregar nuevos productos: ")

def pagina_principal(request):
    
    return HttpResponse("Bienvenidos a tu dia de Shopping, desde la comodidad de tu casa. ")

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            registrado = True
            # Redirigir según el tipo de usuario
            if usuario.tipo_usuario == 'admin':
                return redirect('agregar_producto')
            else:
                return redirect('pagina_principal')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'usuarios/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            contrasena = form.cleaned_data['contrasena']
            usuario = authenticate(request, email=email, password=contrasena)
            if usuario is not None:
                login(request, usuario)
                return redirect('pagina_principal')  # Redirigir a la página principal
            else:
                # Manejar el caso de credenciales inválidas
                return render(request, 'usuarios/inicio_sesion.html', {'form': form, 'error_message': 'Credenciales inválidas'})
    else:
        form = LoginForm()

    return render(request, 'usuarios/inicio_sesion.html', {'form': form})