from django.db import models

class Ingrediente(models.Model):
    TIPO_INGREDIENTE_CHOICES = [
        ('fruta', 'Fruta'),
        ('cobertura', 'Cobertura'),
        ('calda', 'Calda'),
    ]
    
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPO_INGREDIENTE_CHOICES)
    preco_adicional = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome
