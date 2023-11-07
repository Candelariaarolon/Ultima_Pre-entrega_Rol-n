from django.db import models

# Create your models here.


class PrendasRopa(models.Model):
    Marca = models.Charfield(max_length=30)
    Talle = models.IntegerField
    Descripcion = models.Textfield()
    Temporada = models.IntegerField