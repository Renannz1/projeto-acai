from django.contrib import admin
from .models import Sabor, Acompanhamento, Tamanho

@admin.register(Sabor)
class SaborAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco_adicional')
    search_fields = ('nome',)

@admin.register(Acompanhamento)
class AcompanhamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco_adicional')
    search_fields = ('nome',)

@admin.register(Tamanho)
class TamanhoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco_adicional')
    search_fields = ('nome',)
