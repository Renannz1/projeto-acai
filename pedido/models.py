from django.db import models
from produto.models import Produto
from ingrediente.models import Ingrediente


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