from django.db import models
from produto.models import Produto
from ingrediente.models import Ingrediente, Tamanho

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
    
class PedidoPersonalizado(models.Model):
    ingredientes = models.ManyToManyField(Ingrediente)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def calcular_total(self):
        total_ingredientes = sum(ingrediente.preco_adicional for ingrediente in self.ingredientes.all())
        total = total_ingredientes + self.tamanho.preco_adicional
        return total * self.quantidade

    def __str__(self):
        ingredientes_list = ", ".join([ingrediente.nome for ingrediente in self.ingredientes.all()])
        return f"Pedido de {self.quantidade}x Açaí com {ingredientes_list} ({self.tamanho.nome})"
