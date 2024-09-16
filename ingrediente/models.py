from django.db import models

class Sabor(models.Model):
    nome = models.CharField(max_length=100)
    preco_adicional = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.nome} (+R$ {self.preco_adicional})"


class Acompanhamento(models.Model):
    nome = models.CharField(max_length=100)
    preco_adicional = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.nome} (+R$ {self.preco_adicional})"


class Tamanho(models.Model):
    nome = models.CharField(max_length=50)  
    preco_adicional = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.nome} (+R$ {self.preco_adicional})"
