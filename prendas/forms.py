from django import forms
from .models import PrendasRopa

class PrendaForm(forms.ModelForm):
    class Meta:
        model = PrendasRopa
        fields = ['Titulo', 'Marca', 'Descripcion', 'Vendedor', 'Fecha', 'Precio']