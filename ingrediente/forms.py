from django import forms
from .models import Acompanhamento, Sabor, Tamanho

class AcompanhamentoForm(forms.ModelForm):
    class Meta:
        model = Acompanhamento  # Alterado para Acompanhamento
        fields = ['nome', 'preco_adicional']

class SaborForm(forms.ModelForm):
    class Meta:
        model = Sabor
        fields = ['nome', 'preco_adicional']

class TamanhoForm(forms.ModelForm):
    class Meta:
        model = Tamanho
        fields = ['nome', 'preco_adicional']
