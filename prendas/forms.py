from django import forms
from .models import PrendasRopa

class PrendaForm(forms.ModelForm):
    class Meta:
        model = PrendasRopa
        fields = ['Titulo', 'Marca', 'Descripcion', 'Vendedor', 'Fecha', 'Precio']
        
from django import forms

class ComentarioForm(forms.Form):
    comentario = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'placeholder': 'Escribe tu comentario aquí'}))
