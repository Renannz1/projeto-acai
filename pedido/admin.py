from django.contrib import admin
from .models import PedidoProduto, PedidoPersonalizado

class PedidoProdutoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'tamanho', 'quantidade', 'usuario', 'status', 'data_pedido')
    list_filter = ('status', 'usuario')

class PedidoPersonalizadoAdmin(admin.ModelAdmin):
    list_display = ('sabor', 'tamanho', 'quantidade', 'usuario', 'status', 'data_pedido')
    list_filter = ('status', 'usuario')

admin.site.register(PedidoProduto, PedidoProdutoAdmin)
admin.site.register(PedidoPersonalizado, PedidoPersonalizadoAdmin)
