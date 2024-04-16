from categorias.models import Categoria
from post.models import Post

def categorias(request):
    categorias = Categoria.objects.all()
    return {'categorias': categorias}

def postagens(request):
    postagens = Post.objects.all()
    return {'postagens': postagens}

def dados_do_usuario(request):
    usuario = request.user
    dados_usuario = {}
    if usuario.is_authenticated:
        dados_usuario = {
            'nome': usuario.username,
            'email': usuario.email,
        }
    return {'usuario': dados_usuario}
