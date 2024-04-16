from django.contrib import admin
from .models import Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['titulo']
    list_filter = ['titulo']
    search_fields = ['titulo']
    prepopulated_fields = {'slug': ('titulo',)}
    ordering = ['titulo']