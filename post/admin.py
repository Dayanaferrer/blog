from django import forms
from django.contrib import admin
from post.models import Post, Comentario

@admin.register(Post)
class criarPostagemAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'dt_criacao', 'usuario', 'imagem']
    search_fields = ['titulo', 'categoria']
    list_per_page = 8
    list_editable = ['imagem']
    prepopulated_fields = {'slug': ('titulo',)}


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'autor', 'dt_criacao', 'status', 'post']
    search_fields = ['autor__username', 'post__titulo']
    list_editable = ['status']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['autor'].queryset = form.base_fields['autor'].queryset.filter(is_staff=True)
        return form