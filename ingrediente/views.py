from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingrediente, Tamanho
from .forms import IngredienteForm, TamanhoForm



# -----------------------------------------------------------------------------------
def listar_ingredientes(request):
    tamanhos = Tamanho.objects.all()
    ingredientes = Ingrediente.objects.all()
    return render(request, 'ingrediente/listar_ingredientes.html', {'ingredientes': ingredientes, 'tamanhos': tamanhos})

def adicionar_ingrediente(request):
    if request.method == 'POST':
        form = IngredienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_ingredientes')
    else:
        form = IngredienteForm()
    return render(request, 'ingrediente/adicionar_ingrediente.html', {'form': form})

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

def remover_ingrediente(request, ingrediente_id):
    ingrediente = get_object_or_404(Ingrediente, id=ingrediente_id)
    if request.method == 'POST':
        ingrediente.delete()
        return redirect('listar_ingredientes')
    return render(request, 'ingrediente/remover_ingrediente.html', {'ingrediente': ingrediente})
# -----------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------

def listar_tamanhos(request):
    tamanhos = Tamanho.objects.all()
    return render(request, 'ingrediente/listar_tamanhos.html', {'tamanhos': tamanhos})


def adicionar_tamanho(request):
    if request.method == 'POST':
        form = TamanhoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_ingredientes')
    else:
        form = TamanhoForm()
    return render(request, 'ingrediente/adicionar_tamanho.html', {'form': form})

def editar_tamanho(request, tamanho_id):
    tamanho = get_object_or_404(Tamanho, id=tamanho_id)
    if request.method == 'POST':
        form = TamanhoForm(request.POST, instance=tamanho)
        if form.is_valid():
            form.save()
            return redirect('listar_ingredientes')
    else:
        form = TamanhoForm(instance=tamanho)
    return render(request, 'ingrediente/editar_tamanho.html', {'form': form})

def remover_tamanho(request, tamanho_id):
    tamanho = get_object_or_404(Tamanho, id=tamanho_id)
    if request.method == 'POST':
        tamanho.delete()
        return redirect('listar_ingredientes')
    return render(request, 'ingrediente/remover_tamanho.html', {'tamanho': tamanho})
# -----------------------------------------------------------------------------------
