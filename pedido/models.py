from django.db import models
from produto.models import Produto
from ingrediente.models import Sabor, Acompanhamento, Tamanho

class PedidoProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    data_pedido = models.DateTimeField(auto_now_add=True)
    
    METODOS_PAGAMENTO = [
        ('pagamento_na_entrega', 'Pagar na Entrega'),
    ]
    metodo_pagamento = models.CharField(max_length=20, choices=METODOS_PAGAMENTO, default='pagamento_na_entrega')
    
    STATUS_PEDIDO = [
        ('pendente', 'Pendente'),
        ('confirmado', 'Confirmado'),
        ('em_transito', 'Em Trânsito'),
        ('entregue', 'Entregue'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_PEDIDO, default='pendente')

    def calcular_total(self):
        total = self.produto.preco + self.tamanho.preco_adicional
        return total * self.quantidade

    def __str__(self):
        return f"Pedido de {self.quantidade}x {self.produto.nome} ({self.tamanho.nome})"
    

class PedidoPersonalizado(models.Model):
    sabor = models.ForeignKey(Sabor, on_delete=models.CASCADE)
    acompanhamentos = models.ManyToManyField(Acompanhamento, blank=True)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    data_pedido = models.DateTimeField(auto_now_add=True)

    METODOS_PAGAMENTO = [
        ('pagamento_na_entrega', 'Pagar na Entrega'),
    ]
    metodo_pagamento = models.CharField(max_length=20, choices=METODOS_PAGAMENTO, default='pagamento_na_entrega')

    STATUS_PEDIDO = [
        ('pendente', 'Pendente'),
        ('confirmado', 'Confirmado'),
        ('em_transito', 'Em Trânsito'),
        ('entregue', 'Entregue'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_PEDIDO, default='pendente')

    def calcular_total(self):
        total_acompanhamentos = sum(acomp.preco_adicional for acomp in self.acompanhamentos.all())
        total = self.sabor.preco_adicional + total_acompanhamentos + self.tamanho.preco_adicional
        return total * self.quantidade

    def __str__(self):
        acompanhamentos_list = ", ".join([acomp.nome for acomp in self.acompanhamentos.all()])
        return f"Pedido de {self.quantidade}x Açaí de {self.sabor.nome} com {acompanhamentos_list} ({self.tamanho.nome})"
