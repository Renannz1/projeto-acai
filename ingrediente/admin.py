from django.contrib import admin
from .models import Ingrediente

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'preco_adicional')  
    search_fields = ['nome'] 
    list_filter = ['tipo']  
