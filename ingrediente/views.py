from django.shortcuts import render, redirect, get_object_or_404
from .models import Acompanhamento, Tamanho, Sabor
from .forms import AcompanhamentoForm, TamanhoForm, SaborForm

# ------------- lista todos os ingredientes -------------
def listar_ingredientes(request):
    acompanhamentos = Acompanhamento.objects.all()
    tamanhos = Tamanho.objects.all()
    sabores = Sabor.objects.all()
    return render(request, 'ingrediente/listar_ingredientes.html', {'acompanhamentos': acompanhamentos, 'tamanhos': tamanhos, 'sabores': sabores})

# ------------- Acompanhamentos -------------
def adicionar_acompanhamento(request):
    if request.method == 'POST':
        form = AcompanhamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_ingredientes')
    else:
        form = AcompanhamentoForm()
    return render(request, 'ingrediente/adicionar_acompanhamento.html', {'form': form})

def editar_acompanhamento(request, acompanhamento_id):
    acompanhamento = get_object_or_404(Acompanhamento, id=acompanhamento_id)
    if request.method == 'POST':
        form = AcompanhamentoForm(request.POST, instance=acompanhamento)
        if form.is_valid():
            form.save()
            return redirect('listar_ingredientes')
    else:
        form = AcompanhamentoForm(instance=acompanhamento)
    return render(request, 'ingrediente/editar_acompanhamento.html', {'form': form})

def remover_acompanhamento(request, acompanhamento_id):
    acompanhamento = get_object_or_404(Acompanhamento, id=acompanhamento_id)
    if request.method == 'POST':
        acompanhamento.delete()
        return redirect('listar_ingredientes')
    return render(request, 'ingrediente/remover_acompanhamento.html', {'acompanhamento': acompanhamento})


# ------------- Sabores -------------
def adicionar_sabor(request):
    if request.method == 'POST':
        form = SaborForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_ingredientes')
    else:
        form = SaborForm()
    return render(request, 'ingrediente/adicionar_sabor.html', {'form': form})

def editar_sabor(request, sabor_id):
    sabor = get_object_or_404(Sabor, id=sabor_id)
    if request.method == 'POST':
        form = SaborForm(request.POST, instance=sabor)
        if form.is_valid():
            form.save()
            return redirect('listar_ingredientes')
    else:
        form = SaborForm(instance=sabor)
    return render(request, 'ingrediente/editar_sabor.html', {'form': form})

def remover_sabor(request, sabor_id):
    sabor = get_object_or_404(Sabor, id=sabor_id)
    if request.method == 'POST':
        sabor.delete()
        return redirect('listar_ingredientes')
    return render(request, 'ingrediente/remover_sabor.html', {'sabor': sabor})


# ------------- Tamanhos -------------
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
