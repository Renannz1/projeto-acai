from django.db import models

class Ingrediente(models.Model):
    TIPO_INGREDIENTE_CHOICES = [
        ('acompanhamento', 'Acompanhamento'),
        ('sabor', 'Sabor'),
    ]
    
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPO_INGREDIENTE_CHOICES)
    preco_adicional = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome


class Tamanho(models.Model):
    nome = models.CharField(max_length=50)  
    preco_adicional = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.nome} (+R$ {self.preco_adicional})"
