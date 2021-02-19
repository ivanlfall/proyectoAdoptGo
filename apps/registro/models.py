from django.db import models

# Create your models here.
class Usuario(models.Model):
    apellido = models.CharField(max_length=15)
    nombre = models.CharField(max_length=15)
    edad = models.IntegerField()
    email = models.EmailField()
    denunciado = models.BooleanField()

class Posteo(models.Model):
    nombre_mascota = models.CharField(max_length=15)
    animal = models.CharField(max_length=15)
    edad = models.IntegerField()
    descripcion = models.CharField(max_length=140)
    fecha = models.DateField()
    disponible = models.BooleanField()
    postulantes = models.ManyToManyField(Usuario)
