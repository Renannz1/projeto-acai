from django.db import models

from ingrediente.models import Ingrediente

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    ingredientes = models.ManyToManyField(Ingrediente, blank=True)  

    def __str__(self):
        return self.nome