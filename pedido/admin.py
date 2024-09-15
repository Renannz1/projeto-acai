from django.contrib import admin
from .models import PedidoProduto

@admin.register(PedidoProduto)
class PedidoProdutoAdmin(admin.ModelAdmin):
    list_display = ['produto', 'nome_tamanho', 'quantidade', 'data_pedido', 'preco_final']
    search_fields = ['produto__nome', 'tamanho__nome']
    list_filter = ['data_pedido', 'tamanho']

    def nome_tamanho(self, obj):
        return obj.tamanho.nome
    nome_tamanho.short_description = 'Tamanho'

    def preco_final(self, obj):
        return f"R$ {obj.calcular_total():.2f}"
    preco_final.short_description = 'Preço Final'
