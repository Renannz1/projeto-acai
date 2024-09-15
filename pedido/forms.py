from django import forms
from .models import PedidoProduto
from produto.models import Produto
from ingrediente.models import Tamanho


class PedidoProdutoForm(forms.ModelForm):
    produto = forms.ModelChoiceField(queryset=Produto.objects.all(), required=True, label="Escolha o Açaí Pronto")
    tamanho = forms.ModelChoiceField(queryset=Tamanho.objects.all(), required=True, label="Escolha o Tamanho")
    quantidade = forms.IntegerField(min_value=1, label="Quantidade", initial=1)

    class Meta:
        model = PedidoProduto
        fields = ['produto', 'tamanho', 'quantidade']