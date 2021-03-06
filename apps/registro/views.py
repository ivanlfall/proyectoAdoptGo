from django.contrib.auth.models import User
from apps.registro.models import CustomUserForm, Denuncia, Posteo, ReferenciaUsuario
from django.shortcuts import render
from django.db.models import Q
import datetime
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def mostrar_posteo(request):

    mascota_buscada = request.GET.get('buscarMascota')
    posteos = Posteo.objects.all()
    if mascota_buscada:

        posteos = Posteo.objects.filter(
            Q(animal = mascota_buscada)
        ).distinct()

    return render(
        request,
        'inicio.html',
        {
            'posteos' : posteos
        }
    )



def nuevoPost(request):
    if request.method == 'POST':

        post_ok = True
        nusuario_creador = User.objects.filter(
            id = request.POST.get('userId') 
        )
        nnombre = request.POST.get('nombreMascota')
        nanimal = request.POST.get('tipoAnimal')
        if nanimal.lower() == 'otros':
            nanimal = request.POST.get('otros')
        nedad = request.POST.get('edad')
        ndescripcion = request.POST.get('descripcionPost')
        nfecha = datetime.datetime.now()
        ndisponible = True

        Posteo.objects.create(usuario_creador = nusuario_creador.first() ,nombre_mascota = nnombre, animal = nanimal, edad = nedad, descripcion = ndescripcion, fecha = nfecha, disponible = ndisponible)

        return render(
            request,
            'registro.html',
            {
               'post_ok' : post_ok
            }
        )


    return render(
        request,
        'registro.html',
        {
            
        }
    )

def mi_perfil(request, userId):

    usuario = filtrar(User, userId)
    #  User.objects.filter(
    #         id = userId 
    #     ).first()

    referencia = ReferenciaUsuario.objects.filter(
        usuario = usuario
    )
    sumador = 0
    for ref in referencia:
        sumador += ref.puntaje
    if len(referencia) == 0:
        puntajeTotal = 0
    else:
        puntajeTotal = round(sumador/len(referencia),2)

    return render(
        request,
        'perfilUsuario.html',
        {
            'usuario' : usuario,
            'referencia' : referencia,
            'puntajeTotal' : puntajeTotal
        }
    )

def puntuarUsuario(request):

    comentario = ''
    idUsuario = request.POST.get('idUser')
    if request.method == 'POST':
        usuario = filtrar(User, idUsuario)
        #  User.objects.filter(
        #     id = request.POST.get('idUser')
        # ).first()
        puntuacion = request.POST.get('puntaje')
        comentario += f'\n{request.POST.get("comentario")}'

        ReferenciaUsuario.objects.create(usuario = usuario, puntaje = puntuacion, comentarios = comentario)
        
        comentario_ok = True
        mensaje = 'Tu comentario se ha enviado correctamente'
        return render(
            request,
            'calificarPostulante.html',
            {
                'comentario_ok' : comentario_ok,
                'mensaje' : mensaje
            }
        )
    
    return render(
        request,
        'calificarPostulante.html',
    )

def calificar(request, idPostulante):

    return render(
        request,
        'calificarPostulante.html',
        {
            'usuario' : idPostulante
        }
    )

def formulario_registro_usuario(request):

    data= {
        'form': CustomUserForm()
    }
    if request.method == 'POST':
        formulary = CustomUserForm(request.POST)
        if formulary.is_valid():
            formulary.save()
            username = formulary.cleaned_data['username'] 
            password= formulary.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return render(request, "principal/index.html")       
        else:
            messages.warning(request,"You have entered the wrong values")
    return render(request, 'registroUsuario.html', data)


def postular(request, usuario, posteo):

    postulacion_ok = True
    user = filtrar(User, usuario) 
    # User.objects.filter(
    #         id = usuario 
    #     ).first()
    post = filtrar(Posteo, posteo)
    #  Posteo.objects.filter(
    #     id = posteo
    # ).first()
    mensaje = f'Has ingresado a la lista para adoptar a {post.nombre_mascota}'
    
    post.postulantes += str(user.id)
    print(list(post.postulantes))
    post.save()

    return render(
        request,
        'inicio.html',
        {
            'mensaje' : mensaje,
            'postulacion_ok' : postulacion_ok,
            'post' : post
        }
    )


def denunciar(request, usuario, denunciado):

    userDenunciante = filtrar(User, usuario)
    # User.objects.filter(
    #             id = usuario 
    #         ).first()
    userDenunciado = filtrar(User, denunciado)
    # User.objects.filter(
    #             id = denunciado 
    #         ).first()

    if request.method == 'POST':

        denuncia_ok = True
        denuncia = Denuncia.objects.create(
            usuario_denunciado = userDenunciado, 
            id_usuario_denunciante = userDenunciante.id,
            comentario_denuncia = request.POST.get('comentario') 
        )
        
        denuncia.save()

        mensaje = 'Tu denuncia se ha enviado correctamente.'
        return render(
            request,
            'formularioDenuncia.html',
            {
                'mensaje' : mensaje,
                'denuncia_ok' : denuncia_ok
                
            }
        )
    else:

        return render(
            request,
            'formularioDenuncia.html',
            {
                'userDenunciante' : userDenunciante,
                'userDenunciado' : userDenunciado
            }
        )

def mis_posteos(request, userId):

    mis_posts = True

    usuario = filtrar(User, userId)
    
    lista_posteos = Posteo.objects.filter(
        usuario_creador = usuario
    )
    

    return render(
        request,
        'perfilUsuario.html',
        {
            'mis_posts' : mis_posts,
            'lista_posteos' : lista_posteos
        }
    )

def verPostulantes(request, idPost):
    
    post = filtrar(Posteo, idPost)

    lista_postulantes = []
    for postulante in post.postulantes:

        lista_postulantes.append(
            User.objects.filter(
                id = int(postulante)
            ).first()
        )

    return render(
        request,
        'verPostulantes.html',
        {
            'lista_postulantes' : lista_postulantes,
            'post' : post
        }
    )

def adopcionCompletada(request, idPost):

    adoptado = True

    post = filtrar(Posteo, idPost)

    post.disponible = False
    post.save()
    mensaje = 'El adoptante fué asignado'
    return render(
        request,
        'verPostulantes.html',
        {
            'mensaje' : mensaje,
            'adoptado' : adoptado
        }
    )

def filtrar(objeto, id):

    return objeto.objects.filter(
        id = id 
    ).first()