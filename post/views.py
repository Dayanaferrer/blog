from django.http import Http404
from django.shortcuts import redirect, render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer  
from .models import Comentario, Post as criarPost
from post.forms import PostForm, ComentarioForm
from categorias.models import Categoria
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def postagem_detalhada(request, pk):
    postagem = get_object_or_404(criarPost, pk=pk)
    comentarios = postagem.comentario_set.all()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False, user=request.user)
            comentario.post = postagem
            comentario.save()
            messages.success(request, 'Comentário adicionado com sucesso.')
            return redirect('postagem_detalhada', pk=pk)
        else:
            messages.error(request, 'Ocorreu um erro ao adicionar o comentário.')
    else:
        form = ComentarioForm()

    paginator = Paginator(comentarios, 3)
    page_number = request.GET.get('page')
    comentarios_paginados = paginator.get_page(page_number)

    return render(request, 'galeria/postagem_detalhada.html', {'form': form, 'postagem': postagem, 'comentarios': comentarios_paginados})

@login_required
def gerenciar_postagem(request):
    postagens_usuario = criarPost.objects.filter(usuario=request.user)
    contexto = {
        'postagens_usuario': postagens_usuario
    }
    return render(request, 'galeria/postagemdousuario.html', contexto)


@login_required
def editar_postagem(request, pk):
    postagem = criarPost.objects.get(pk=pk)
    form = PostForm(request.POST or None, instance=postagem)
    sucesso = False
    if form.is_valid():
        form.save()
        sucesso = True
        return redirect('postagem_detalhada', pk=postagem.pk)
    contexto = {
        'postagem': postagem,
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'galeria/editar_postagem.html', contexto)
 
@login_required 
def criar_postagem(request):
    template_name = 'galeria/criar_postagem.html'
    categorias = Categoria.objects.all()
    postagem = criarPost.objects.all()
    sucesso = False
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES)
        
        if form.is_valid():
            post = form.save(False)
            post.usuario = request.user
            post.slug = form.cleaned_data['titulo'].replace(' ', '-').lower()
            post.save()
            sucesso = True
            return redirect('postagem_detalhada', pk=post.pk)
        else:
            print(form.errors)
            raise Http404  
    else:
            form = PostForm()
    contexto = {
        'postagem': postagem,
        'form': form,
        'sucesso': sucesso,
        'categorias': categorias
    }
    return render(request, template_name, contexto)

@login_required
def excluir_postagem(request, pk):
    postagem = criarPost.objects.get(pk=pk)
    if request.method == 'POST':
        postagem.delete()
        messages.success(request, 'A postagem foi excluída com sucesso.')
        return redirect('gerenciar_postagem')
    return render(request, 'galeria/postagemdousuario.html')

@login_required
def adicionar_comentario(request, pk):
    postagem = get_object_or_404(criarPost, pk=pk)

    if request.method == 'POST':
        form = ComentarioForm(request.POST, user=request.user)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = postagem
            comentario.autor = request.user
            comentario.save()
            messages.success(request, 'Comentário adicionado com sucesso.')
            return redirect('postagem_detalhada', pk=pk)
        else:
            messages.error(request, 'Ocorreu um erro ao adicionar o comentário.')
    else:
        form = ComentarioForm(user=request.user)
        
    comentarios = postagem.comentario_set.all()
    paginator = Paginator(comentarios, 3) 
    page_number = request.GET.get('page')
    try:
        comentarios_paginados = paginator.page(page_number)
    except PageNotAnInteger:
        comentarios_paginados = paginator.page(1)
    except EmptyPage:
        comentarios_paginados = paginator.page(paginator.num_pages)

    return render(request, 'galeria/postagem_detalhada.html', {'form': form, 'postagem': postagem, 'comentarios': comentarios_paginados})
    
def listar_postagens(request):    
    return render(request, 'galeria/lista_postagens.html')
   
def buscar_posts(request):
    if request.method == "POST":
        searched = request.POST['searched'] 
        postagens = criarPost.objects.filter(titulo__contains=searched) 
        return render(request, 'galeria/resultado_busca.html', {'searched': searched, 'postagens': postagens})
    else: 
        return render(request, 'galeria/resultado_busca.html')

class PostagemViewSet(ModelViewSet):
    queryset = criarPost.objects.all()
    serializer_class = PostSerializer
