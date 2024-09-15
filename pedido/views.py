from django.shortcuts import render, get_object_or_404, redirect

from produto.models import Produto
from .models import PedidoProduto
from .forms import PedidoProdutoForm

def listar_index(request):
    produtos = Produto.objects.all()
    return render(request, 'pedido/index.html', {'produtos': produtos})

def fazer_pedido(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = PedidoProdutoForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            return redirect('resumo_pedido', pedido_id=pedido.id)
    else:
        form = PedidoProdutoForm(initial={'produto': produto})
    return render(request, 'pedido/fazer_pedido.html', {'form': form, 'produto': produto})

def resumo_pedido(request, pedido_id):
    pedido = get_object_or_404(PedidoProduto, id=pedido_id)
    total_final = pedido.calcular_total()
    return render(request, 'pedido/resumo_pedido.html', {'pedido': pedido, 'total_final': total_final})
