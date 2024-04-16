from django.db import models
from django.contrib.auth.models import User   
class Squad(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imagens/', blank=True)
    linkedin = models.CharField(max_length=250)
    github = models.CharField(max_length=250)

    def __str__(self):
        return self.nome

