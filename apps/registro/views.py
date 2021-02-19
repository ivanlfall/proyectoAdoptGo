from apps.registro.models import Posteo
from django.shortcuts import render


# Create your views here.
def mostrar_posteo(request):

    posteos = Posteo.objects.all()

    return render(
        request,
        'inicio.html',
        {
            'posteos' : posteos
        }
    )

def nuevoPost(request):

    return render(
        request,
        'registro.html',
        {
            
        }
    )

def postear(request): # Con este método vamos a cargar los nuevos post

    return render()