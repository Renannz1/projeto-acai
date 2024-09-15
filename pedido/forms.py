from django import forms
from .models import PedidoProduto
from ingrediente.models import Tamanho

class PedidoProdutoForm(forms.ModelForm):
    tamanho = forms.ModelChoiceField(queryset=Tamanho.objects.all(), required=True, label="Escolha o Tamanho")
    quantidade = forms.IntegerField(min_value=1, label="Quantidade", initial=1)

    class Meta:
        model = PedidoProduto
        fields = ['tamanho', 'quantidade']
