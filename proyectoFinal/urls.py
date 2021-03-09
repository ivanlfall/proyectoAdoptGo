"""proyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from apps.registro.views import adopcionCompletada, denunciar, formulario_registro_usuario, mi_perfil, mis_posteos, mostrar_posteo, nuevoPost, postular, verPostulantes
from proyectoFinal.views import contacto, inicio, nosotros
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', inicio, name= 'inicio'),
    path('accounts/', include('django.contrib.auth.urls' ), name='login'), 
    path('registroUsuario/', formulario_registro_usuario, name= 'registroUsuario'),
    path('nuevoPost/', nuevoPost, name= 'nuevoPost'),
    path('contacto/', contacto, name= 'contacto'),
    path('nosotros/', nosotros, name= 'nosotros'),
    path(r'^miperfil/(?P<userId>\d+)/$', mi_perfil, name= 'miperfil'),
    path(r'^denunciar/(?P<usuario>\d+)/(?P<denunciado>\d+)/$', denunciar, name= 'denunciar'),
    path(r'^mis_posteos/(?P<userId>\d+)/$', mis_posteos, name= 'mis_posteos'),
    path(r'^postular/(?P<usuario>\d+)/(?P<posteo>\d+)/$', postular, name= 'postular'),
    path('mostrar_posteo/', mostrar_posteo, name= 'mostrar_posteo'),
    path(r'^postulantes/(?P<idPost>\d+)/$', verPostulantes, name= 'verPostulantes'),
    path(r'^adoptado/(?P<idPost>\d+)/$', adopcionCompletada, name= 'adoptado'),
]
