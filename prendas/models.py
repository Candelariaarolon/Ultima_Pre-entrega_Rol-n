from django.db import models

# Create your models here.


class PrendasRopa(models.Model):
    Marca = models.CharField(max_length=30)
    Talle = models.IntegerField
    Descripcion = models.TextField()
    Temporada = models.IntegerField