from django.shortcuts import get_object_or_404, render
from post.models import Post
from inicio.models import Squad

def inicio(request):
    postagens = Post.objects.order_by('-dt_criacao')    
    return render(request, 'galeria/inicio.html', {'postagens': postagens})

def sobre(request):    
    return render(request, 'galeria/sobre.html')

def contato(request):
    squads = Squad.objects.all()
    return render(request, 'galeria/contato.html', {'squads': squads})
