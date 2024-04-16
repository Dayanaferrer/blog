from django.shortcuts import render
from post.models import Post
from inicio.models import Squad
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def inicio(request):
    todas_postagens = Post.objects.order_by('-dt_criacao')
    paginator = Paginator(todas_postagens, 2)  
    numero_pagina = request.GET.get('pagina')
    try:
        postagens = paginator.page(numero_pagina)
    except PageNotAnInteger:
        postagens = paginator.page(1)
    except EmptyPage:
        postagens = paginator.page(paginator.num_pages)
    return render(request, 'galeria/inicio.html', {'postagens': postagens})

def sobre(request):    
    return render(request, 'galeria/sobre.html')

def contato(request):
    squads = Squad.objects.all()
    return render(request, 'galeria/contato.html', {'squads': squads})
