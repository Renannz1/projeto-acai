from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone', 'endereco')  # Colunas que aparecerão no admin
    search_fields = ['nome', 'cpf']  # Campos de busca
