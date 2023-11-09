from django.db import models

class Pago(models.Model):
    user = models.CharField(max_length=30)
    medio_pago = models.CharField(max_length=20, choices=[('efectivo', 'Efectivo'), ('debito', 'Tarjeta de Débito'), ('credito', 'Tarjeta de Crédito')])
    numero_tarjeta = models.CharField(max_length=16)
    codigo_seguridad = models.CharField(max_length=3)

    def __str__(self):
        return self.user.username
