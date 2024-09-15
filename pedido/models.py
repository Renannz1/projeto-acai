from django.db import models
from django.contrib.auth.models import User
from ingrediente.models import Ingrediente, Tamanho
from produto.models import Produto



class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    preco_total = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, null=True, blank=True, on_delete=models.CASCADE)  
    ingredientes = models.ManyToManyField(Ingrediente, blank=True)  
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def calcular_preco(self):
        if self.produto:  # Se for um produto pronto
            preco_base = self.produto.preco
        else:  # Se for um açaí personalizado
            preco_base = sum([ingrediente.preco_adicional for ingrediente in self.ingredientes.all()])

        return (preco_base + self.tamanho.preco_adicional) * self.quantidade

    def __str__(self):
        return f"Item #{self.id} do Pedido {self.pedido}"










'''
class PedidoAcaiPronto(models.Model):
    acai_pronto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def calcular_preco_total(self):
        return self.acai_pronto.preco * self.quantidade

    def save(self, *args, **kwargs):
        self.preco_total = self.calcular_preco_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido de {self.acai_pronto.nome} - Quantidade: {self.quantidade}"



class PedidoAcaiPersonalizado(models.Model):
    ingredientes = models.ManyToManyField(Ingrediente)
    quantidade = models.PositiveIntegerField()
    preco_total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def calcular_preco_total(self):
        total = sum(ingrediente.preco_adicional for ingrediente in self.ingredientes.all())
        return total * self.quantidade

    def save(self, *args, **kwargs):
        self.preco_total = self.calcular_preco_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido personalizado - Quantidade: {self.quantidade}"
'''