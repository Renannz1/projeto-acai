from django.contrib import admin
from .models import PedidoProduto, PedidoPersonalizado

@admin.register(PedidoProduto)
class PedidoProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'tamanho', 'quantidade', 'data_pedido', 'metodo_pagamento', 'status')
    list_filter = ('status', 'produto', 'tamanho')
    search_fields = ('produto__nome', 'tamanho__nome', 'status')
    list_editable = ('status',)

@admin.register(PedidoPersonalizado)
class PedidoPersonalizadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'sabor', 'tamanho', 'quantidade', 'data_pedido', 'metodo_pagamento', 'status')
    list_filter = ('status', 'sabor', 'tamanho')
    search_fields = ('sabor__nome', 'tamanho__nome', 'status')
    list_editable = ('status',)
