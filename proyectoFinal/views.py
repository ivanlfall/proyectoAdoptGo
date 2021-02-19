from django.shortcuts import render

def inicio(request):

    return render(
        request,
        'principal/index.html',
        {
            
        }
    )

def nosotros(request):

    return render(
        request,
        'nosotros.html'
    )

def contacto(request):

    return render(
        request,
        'contacto.html'
    )

