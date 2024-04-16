from django import forms
from .models import Post, Comentario
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):        
    class Meta:
        model = Post
        fields = ['categoria',  'titulo', 'descricao', 'imagem', 'texto']
        list_display = ('id', 'autor', 'texto', 'imagem')
        list_display_links = ('id', 'titulo')
        search_fields = ('autor', 'texto')
        list_filter = ('autor', 'texto')
        list_editable = ('imagem',)

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario']
        labels = {
            'comentario': 'Conteúdo do Comentário'
        }

    def save(self, commit=True, user=None, *args, **kwargs):
        instance = super().save(commit=False)
        instance.autor = user
        if commit:
            instance.save()
        return instance

   
    
       