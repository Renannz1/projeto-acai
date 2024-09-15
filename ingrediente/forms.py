from django import forms
from .models import Ingrediente, Tamanho

class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nome', 'tipo', 'preco_adicional']

class TamanhoForm(forms.ModelForm):
    class Meta:
        model = Tamanho
        fields = ['nome', 'preco_adicional']

