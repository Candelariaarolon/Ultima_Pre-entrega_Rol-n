from django.db import models
from django.contrib.auth.models import User

class PrendasRopa(models.Model):
   # foto = models.ImageField(upload_to='prendas/')
    Titulo = models.CharField(max_length=200, default='Título predeterminado')
    Marca = models.CharField(max_length=200, default='Marca predeterminada')
    Vendedor= models.CharField(max_length=200, default='Nombre de vendedor')
    Descripcion = models.TextField(default='Descripción predeterminada')
    Fecha = models.DateField(default='2024-01-01')  
    Precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
 
    def __str__(self):
        return self.Titulo