# meuapp/context_processors.py

from post.models import Post
from categorias.models import Categoria

def postagens_e_categorias(request):
    postagens = Post.objects.all()
    categorias = Categoria.objects.all()
    return {'postagens': postagens, 'categorias': categorias}

def dados_do_usuario(request):
    usuario = request.user
    dados_usuario = {}
    if usuario.is_authenticated:
        dados_usuario = {
            'nome': usuario.username,
            'email': usuario.email,
        }
    return {'usuario': dados_usuario}
