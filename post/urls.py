from django.urls import path
from post.views import criar_postagem, gerenciar_postagem, postagem_detalhada, editar_postagem, excluir_postagem, buscar_posts

urlpatterns = [
    path('post/criar_postagem/', criar_postagem, name='criar_postagem'),
    path('post/gerenciar_postagem/', gerenciar_postagem, name='gerenciar_postagem'), #OK
    path('post/<int:pk>/', postagem_detalhada, name='postagem_detalhada'), #OK
    path('post/<int:pk>/editar_postagem/', editar_postagem, name='editar_postagem'),
    path('post/<int:pk>/excluir_postagem/', excluir_postagem, name='excluir_postagem'),
    path('buscar_posts/', buscar_posts, name="buscar_posts" )
]