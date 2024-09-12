from django.shortcuts import get_object_or_404, render, redirect
from .models import PedidoAcaiPersonalizado, PedidoAcaiPronto
from .forms import PedidoAcaiPersonalizadoForm, PedidoAcaiProntoForm

def fazer_pedido_acai_pronto(request):
    if request.method == 'POST':
        form = PedidoAcaiProntoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.usuario = request.user
            pedido.save()
            return redirect('resumo_pedido_pronto', pedido_id=pedido.id)
    else:
        form = PedidoAcaiProntoForm()
    
    return render(request, 'pedido/pedido_acai_pronto.html', {'form': form})


def fazer_pedido_acai_personalizado(request):
    if request.method == 'POST':
        form = PedidoAcaiPersonalizadoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.usuario = request.user
            pedido.save()
            form.save_m2m()  # para salvar os ingredientes selecionados na relação m2m
            return redirect('resumo_pedido_personalizado', pedido_id=pedido.id)
    else:
        form = PedidoAcaiPersonalizadoForm()
    
    return render(request, 'pedido/pedido_acai_personalizado.html', {'form': form})


def resumo_pedido_pronto(request, pedido_id):
    pedido = get_object_or_404(PedidoAcaiPronto, id=pedido_id)
    return render(request, 'resumo_acai_pronto.html', {'pedido': pedido})

def resumo_pedido_personalizado(request, pedido_id):
    pedido = get_object_or_404(PedidoAcaiPersonalizado, id=pedido_id)
    return render(request, 'resumo_acai_personalizado.html', {'pedido': pedido})


