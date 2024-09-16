from django import forms
from .models import PedidoPersonalizado, PedidoProduto
from ingrediente.models import Sabor, Acompanhamento, Tamanho

class PedidoProdutoForm(forms.ModelForm):
    tamanho = forms.ModelChoiceField(queryset=Tamanho.objects.all(), required=True, label="Escolha o Tamanho")
    quantidade = forms.IntegerField(min_value=1, label="Quantidade", initial=1)

    class Meta:
        model = PedidoProduto
        fields = ['tamanho', 'quantidade']


class PedidoPersonalizadoForm(forms.ModelForm):
    sabor = forms.ModelChoiceField(
        queryset=Sabor.objects.all(),
        required=True,
        label="Escolha o Sabor"
    )
    acompanhamentos = forms.ModelMultipleChoiceField(
        queryset=Acompanhamento.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Escolha até 4 Acompanhamentos",
    )
    tamanho = forms.ModelChoiceField(queryset=Tamanho.objects.all(), required=True, label="Escolha o Tamanho")
    quantidade = forms.IntegerField(min_value=1, label="Quantidade", initial=1)

    class Meta:
        model = PedidoPersonalizado
        fields = ['sabor', 'acompanhamentos', 'tamanho', 'quantidade']

    def clean_acompanhamentos(self):
        acompanhamentos = self.cleaned_data.get('acompanhamentos')
        if len(acompanhamentos) > 4:
            raise forms.ValidationError("Você pode escolher no máximo 4 acompanhamentos.")
        return acompanhamentos