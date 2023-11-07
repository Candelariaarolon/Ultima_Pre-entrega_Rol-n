from django.db import models


class Usuarios(models.Model):
    nombre = models.Charfield(max_length=30)
    apellido = models.Charfield(max_length=30)
    edad= models.IntegerField

# Create your models here.
