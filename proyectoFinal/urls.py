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
from apps.registro.views import adopcionCompletada, calificar, denunciar, formulario_registro_usuario, mi_perfil, mis_posteos, mostrar_posteo, nuevoPost, postular, puntuarUsuario, verPostulantes
from proyectoFinal.views import contacto, inicio, nosotros
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name= 'inicio'),
    path('accounts/', include('django.contrib.auth.urls' ), name='login'), 
    path('registroUsuario/', formulario_registro_usuario, name= 'registroUsuario'),
    path(
        r'password/rocovery/$',
        auth_views.PasswordResetView.as_view(
            template_name = 'auth/password_reset_form.html',
            html_email_template_name = 'auth/password_reset_email.html',
        ),
        name = 'password_reset'
    ),
    path(
        r'^password/recovery/done/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name='auth/password_reset_done.html',
        ),
        name = 'password_reset_done'
    ),
    path(
        r'^password/recovery/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            post_reset_login=True,
            template_name= 'auth/password_reset_confirm.html',
            post_reset_login_backend=(
                'django.contrib.auth.backends.AllowAllUserModelBackend'
            ),
        ),
        name='password_reset_confirm'
    ),
    path('nuevoPost/', nuevoPost, name= 'nuevoPost'),
    path('contacto/', contacto, name= 'contacto'),
    path('nosotros/', nosotros, name= 'nosotros'),
    path(r'^miperfil/(?P<userId>\d+)/$', mi_perfil, name= 'miperfil'),
    path(r'^calificar/(?P<idPostulante>\d+)/$', calificar, name= 'calificar'),
    path('calificarForm/', puntuarUsuario, name= 'calificarForm'),
    path(r'^denunciar/(?P<usuario>\d+)/(?P<denunciado>\d+)/$', denunciar, name= 'denunciar'),
    path(r'^mis_posteos/(?P<userId>\d+)/$', mis_posteos, name= 'mis_posteos'),
    path(r'^postular/(?P<usuario>\d+)/(?P<posteo>\d+)/$', postular, name= 'postular'),
    path('mostrar_posteo/', mostrar_posteo, name= 'mostrar_posteo'),
    path(r'^postulantes/(?P<idPost>\d+)/$', verPostulantes, name= 'verPostulantes'),
    path(r'^adoptado/(?P<idPost>\d+)/$', adopcionCompletada, name= 'adoptado'),
]
