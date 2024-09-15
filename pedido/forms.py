from django import forms
from .models import PedidoPersonalizado, PedidoProduto
from ingrediente.models import Ingrediente, Tamanho

class PedidoProdutoForm(forms.ModelForm):
    tamanho = forms.ModelChoiceField(queryset=Tamanho.objects.all(), required=True, label="Escolha o Tamanho")
    quantidade = forms.IntegerField(min_value=1, label="Quantidade", initial=1)

    class Meta:
        model = PedidoProduto
        fields = ['tamanho', 'quantidade']


class PedidoPersonalizadoForm(forms.ModelForm):
    ingredientes = forms.ModelMultipleChoiceField(
        queryset=Ingrediente.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Escolha seus Ingredientes"
    )
    tamanho = forms.ModelChoiceField(queryset=Tamanho.objects.all(), required=True, label="Escolha o Tamanho")
    quantidade = forms.IntegerField(min_value=1, label="Quantidade", initial=1)

    class Meta:
        model = PedidoPersonalizado
        fields = ['ingredientes', 'tamanho', 'quantidade']

