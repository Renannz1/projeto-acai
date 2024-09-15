from django import forms
from .models import ItemPedido
from produto.models import Produto
from ingrediente.models import Ingrediente
from .models import Tamanho

class PedidoProdutoForm(forms.ModelForm):
    tamanho = forms.ModelChoiceField(queryset=Tamanho.objects.all(), required=True, label="Escolha o Tamanho")

    class Meta:
        model = ItemPedido
        fields = ['tamanho', 'quantidade']

class PedidoPersonalizadoForm(forms.ModelForm):
    ingredientes = forms.ModelMultipleChoiceField(
        queryset=Ingrediente.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Escolha seus Ingredientes"
    )
    tamanho = forms.ModelChoiceField(queryset=Tamanho.objects.all(), required=True, label="Escolha o Tamanho")

    class Meta:
        model = ItemPedido
        fields = ['ingredientes', 'tamanho', 'quantidade']
