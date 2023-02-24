from django.db import models

# Create your models here.
#cada una de estas, son columnas :)

class Competencia(models.Model):
    nombre = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    fecha = models.DateField()
    inscriptos = models.IntegerField()
    kilometraje = models.IntegerField()
    imagen = models.ImageField(upload_to="placas_rally", null=True, blank=True)


class Piloto(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField(default=17)
    nacionalidad = models.CharField(max_length=20)
    marca_vehiculo = models.CharField(max_length=40)
    modelo_vehiculo = models.CharField(max_length=40)

class Copiloto(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField(default=15)
    nacionalidad = models.CharField(max_length=20)