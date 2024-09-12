from django import forms
from .models import Ingrediente

class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nome', 'tipo', 'preco_adicional']
