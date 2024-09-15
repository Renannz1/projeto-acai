from django.db import models
from produto.models import Produto
from ingrediente.models import Tamanho

class PedidoProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def calcular_total(self):
        total = self.produto.preco + self.tamanho.preco_adicional
        return total * self.quantidade

    def __str__(self):
        return f"Pedido de {self.quantidade}x {self.produto.nome} ({self.tamanho.nome})"
