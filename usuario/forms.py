from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .models import Usuario


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    # Método que faz a validação da senha
    def clean(self):
        # Chama o metodo de limpeza da classe base ModelForm
        cleaned_data = super().clean()
        # obtem os valores dos campos de senha
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("As senhas não conferem.")
        
        # retorna os dados limpos apos a validacao
        return cleaned_data


class UserLoginForm(AuthenticationForm):
    # personalizando os campos 'username' e 'password'
    username = forms.CharField(
        label="Nome de usuário",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'cpf', 'telefone', 'endereco']
