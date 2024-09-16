from django.db import models

from ingrediente.models import Sabor, Acompanhamento

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    sabor = models.ManyToManyField(Sabor, blank=True)  
    acompanhamentos = models.ManyToManyField(Acompanhamento, blank=True)  
 

    def __str__(self):
        return self.nome