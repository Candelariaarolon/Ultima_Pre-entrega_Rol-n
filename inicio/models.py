from django.db import models


class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad= models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.apellido} -  {self.edad}'

# Create your models here.
