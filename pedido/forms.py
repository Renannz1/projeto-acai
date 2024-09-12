from django import forms
from .models import PedidoAcaiPronto, PedidoAcaiPersonalizado, Produto, Ingrediente



class PedidoAcaiProntoForm(forms.ModelForm):
    class Meta:
        model = PedidoAcaiPronto
        fields = ['acai_pronto', 'quantidade']


class PedidoAcaiPersonalizadoForm(forms.ModelForm):
    class Meta:
        model = PedidoAcaiPersonalizado
        fields = ['ingredientes', 'quantidade']
        widgets = {
            'ingredientes': forms.CheckboxSelectMultiple,
        }