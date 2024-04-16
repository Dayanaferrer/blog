from django.db import models
class Categoria(models.Model):
    titulo = models.CharField(max_length=150, null=False)
    slug = models.SlugField(max_length=150, null=False)

    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_atualiacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
