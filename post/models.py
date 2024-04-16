from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User

class Post(models.Model):
    categoria = models.ForeignKey (Categoria, on_delete=models.CASCADE, null=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    titulo = models.CharField(max_length=150, null=False)
    slug = models.SlugField(unique=True, null=True)
    descricao = models.TextField(null=False)
    imagem = models.ImageField(upload_to='imagens/', blank=True, null=True)
    texto = models.TextField(null=False)

    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_atualiacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
class Comentario(models.Model):
    STATUS = (
        ('Lido', 'Lido'),
        ('Não Lido', 'Não Lido'),
    )

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    dt_criacao = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=10, choices=STATUS, default='Não Lido')

    def __str__(self):
        return f'Comentário de {self.autor.username}'