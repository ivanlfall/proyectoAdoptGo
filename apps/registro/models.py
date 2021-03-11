from django.contrib.auth import forms
from django.db import models
from django.db.models.deletion import CASCADE
from django.forms.fields import ImageField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


# Create your models here.
class CustomUserForm(UserCreationForm):
    class Meta :
        model = User
        fields =['username','first_name', 'last_name','email', 'password1', 'password2']

        widgets = {
            'username' : forms.TextInput(attrs = {'class':'form-control mb-3'}),
            'first_name' : forms.TextInput(attrs = {'class':'form-control mb-3'}),
            'last_name' : forms.TextInput(attrs = {'class':'form-control mb-3'}),
            'email' : forms.EmailInput(attrs = {'class':'form-control mb-3'}),
            'password1' : forms.PasswordInput(attrs = {'class':'form-control mb-3'}),
            'password2' : forms.PasswordInput(attrs = {'class':'form-control mb-3'}),
        }


class ReferenciaUsuario(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    puntaje = models.IntegerField()
    comentarios = models.CharField(max_length=1000, blank=True)

class Posteo(models.Model):
    usuario_creador = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nombre_mascota = models.CharField(max_length=15)
    animal = models.CharField(max_length=15)
    edad = models.IntegerField()
    descripcion = models.CharField(max_length=140)
    fecha = models.DateField()
    disponible = models.BooleanField()
    postulantes = models.CharField(max_length=500, blank=True)

    def __str__(self):

        return f'{self.nombre_mascota} - Posteado por: {self.usuario_creador} el día: {self.fecha}'

class Denuncia(models.Model):

    usuario_denunciado = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id_usuario_denunciante = models.IntegerField()
    comentario_denuncia = models.CharField(max_length=250)


    def __str__(self):

        return f'El usuario {self.id_usuario_denunciante} ha denunciado a {self.usuario_denunciado}'
    

