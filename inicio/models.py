from django.db import models


class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad= models.IntegerField(default=0)

# Create your models here.
