from django.contrib import admin
from django.contrib.auth.models import User
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'cpf', 'telefone', 'endereco')
    search_fields = ['user__first_name', 'user__last_name', 'cpf']
