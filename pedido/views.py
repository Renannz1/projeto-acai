from django.shortcuts import render, get_object_or_404, redirect
from .models import PedidoPersonalizado, PedidoProduto
from .forms import MetodoPagamentoForm, PedidoPersonalizadoForm, PedidoProdutoForm
from produto.models import Produto
from django.contrib.auth.decorators import user_passes_test


# ---------- lista os pedidos dos usuarios para alterar o status --------
@user_passes_test(lambda u: u.is_staff)
def listar_pedidos(request):
    pedidos_produto = PedidoProduto.objects.all()
    pedidos_personalizado = PedidoPersonalizado.objects.all()
    return render(request, 'pedido/listar_pedidos.html', {
        'pedidos_produto': pedidos_produto,
        'pedidos_personalizado': pedidos_personalizado,
    })


# ---------- lista as opcoes de pedidos ao usuario --------
def listar_index(request):
    produtos = Produto.objects.all()
    return render(request, 'pedido/index.html', {'produtos': produtos})


# ------- pedido produto pronto --------
def fazer_pedido(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = PedidoProdutoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.produto = produto  
            pedido.save()
            return redirect('resumo_pedido', pedido_id=pedido.id)
    else:
        form = PedidoProdutoForm()
    return render(request, 'pedido/fazer_pedido.html', {'form': form, 'produto': produto})

def resumo_pedido(request, pedido_id):
    pedido = get_object_or_404(PedidoProduto, id=pedido_id)
    total_final = pedido.calcular_total()

    if request.method == 'POST':
        form = MetodoPagamentoForm(request.POST)
        if form.is_valid():
            pedido.metodo_pagamento = form.cleaned_data['metodo_pagamento']
            pedido.status = 'confirmado'
            pedido.save()
            return redirect('pedido_confirmado', pedido_id=pedido.id, tipo_pedido='produto')
    else:
        form = MetodoPagamentoForm()

    return render(request, 'pedido/resumo_pedido.html', {
        'pedido': pedido,
        'total_final': total_final,
        'form': form
    })


# ------- pedido personalizado --------
def fazer_pedido_personalizado(request):
    if request.method == 'POST':
        form = PedidoPersonalizadoForm(request.POST)
        if form.is_valid():
            pedido_personalizado = form.save()
            return redirect('resumo_pedido_personalizado', pedido_id=pedido_personalizado.id)
    else:
        form = PedidoPersonalizadoForm()

    return render(request, 'pedido/fazer_pedido_personalizado.html', {'form': form})

def resumo_pedido_personalizado(request, pedido_id):
    pedido = get_object_or_404(PedidoPersonalizado, id=pedido_id)
    total_final = pedido.calcular_total()

    if request.method == 'POST':
        form = MetodoPagamentoForm(request.POST)
        if form.is_valid():
            pedido.metodo_pagamento = form.cleaned_data['metodo_pagamento']
            pedido.status = 'confirmado'
            pedido.save()
            return redirect('pedido_confirmado', pedido_id=pedido.id, tipo_pedido='personalizado')
    else:
        form = MetodoPagamentoForm()

    return render(request, 'pedido/resumo_pedido_personalizado.html', {
        'pedido': pedido,
        'total_final': total_final,
        'form': form
    })



# ------- pedido confirmado - para os dois tipo de pedido --------
def pedido_confirmado(request, pedido_id, tipo_pedido):
    if tipo_pedido == 'produto':
        pedido = get_object_or_404(PedidoProduto, id=pedido_id)
    elif tipo_pedido == 'personalizado':
        pedido = get_object_or_404(PedidoPersonalizado, id=pedido_id)
    else:
        return render(request, 'pedido/erro.html', {'mensagem': 'Tipo de pedido inválido.'})
    
    return render(request, 'pedido/pedido_confirmado.html', {'pedido': pedido, 'tipo_pedido': tipo_pedido})

# ------- pedido em transito - para os dois tipo de pedido --------


# ---------------------------------------------------------------
def atualizar_status(request, pedido_id, tipo_pedido):
    if tipo_pedido == 'produto':
        pedido = get_object_or_404(PedidoProduto, id=pedido_id)
    elif tipo_pedido == 'personalizado':
        pedido = get_object_or_404(PedidoPersonalizado, id=pedido_id)
    else:
        return render(request, 'pedido/erro.html', {'mensagem': 'Tipo de pedido inválido.'})

    if request.method == 'POST':
        novo_status = request.POST.get('status')
        if novo_status in dict(pedido.STATUS_PEDIDO).keys():  
            pedido.status = novo_status
            pedido.save()

    return redirect('listar_pedidos') 





