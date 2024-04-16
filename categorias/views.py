from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from categorias.models import Categoria
from categorias.serializers import CategoriaSerializer
from post.models import Post

def categoria(request, cats):
    categoria_obj = get_object_or_404(Categoria, titulo=cats)
    categoria_postagens = Post.objects.filter(categoria=categoria_obj).order_by('-dt_criacao')
    return render(request, 'galeria/categoria.html', {'categoria_obj': cats, 'categoria_postagens': categoria_postagens})
class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

