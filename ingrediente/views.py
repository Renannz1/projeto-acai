from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingrediente
from .forms import IngredienteForm

# Listar ingredientes
def listar_ingredientes(request):
    ingredientes = Ingrediente.objects.all()
    return render(request, 'ingrediente/listar_ingredientes.html', {'ingredientes': ingredientes})

# Criar ingrediente
def adicionar_ingrediente(request):
    if request.method == 'POST':
        form = IngredienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_ingredientes')
    else:
        form = IngredienteForm()
    return render(request, 'ingrediente/adicionar_ingrediente.html', {'form': form})

# Editar ingrediente
def editar_ingrediente(request, ingrediente_id):
    ingrediente = get_object_or_404(Ingrediente, id=ingrediente_id)
    if request.method == 'POST':
        form = IngredienteForm(request.POST, instance=ingrediente)
        if form.is_valid():
            form.save()
            return redirect('listar_ingredientes')
    else:
        form = IngredienteForm(instance=ingrediente)
    return render(request, 'ingrediente/editar_ingrediente.html', {'form': form})

# Excluir ingrediente
def remover_ingrediente(request, ingrediente_id):
    ingrediente = get_object_or_404(Ingrediente, id=ingrediente_id)
    if request.method == 'POST':
        ingrediente.delete()
        return redirect('listar_ingredientes')
    return render(request, 'ingrediente/remover_ingrediente.html', {'ingrediente': ingrediente})
