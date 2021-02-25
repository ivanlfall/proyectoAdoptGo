from django import forms

class FormularioNuevoPost(forms.Form):

    nombre = forms.CharField()
    animal = forms.CharField()
    edad = forms.IntegerField()