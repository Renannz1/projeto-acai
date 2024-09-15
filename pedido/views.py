from django.shortcuts import render, get_object_or_404, redirect
from produto.models import Produto
from .models import ItemPedido
from ingrediente.models import Tamanho
from .forms import PedidoProdutoForm



def listar_index(request):
    produtos = Produto.objects.all()
    return render(request, 'pedido/index.html', {'produtos': produtos})

def fazer_pedido(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        form = PedidoProdutoForm(request.POST)
        if form.is_valid():
            item_pedido = form.save(commit=False)
            item_pedido.produto = produto
            item_pedido.save()

            return redirect('resumo_pedido', item_pedido_id=item_pedido.id)
    else:
        form = PedidoProdutoForm()

    return render(request, 'pedido/fazer_pedido.html', {'produto': produto, 'form': form})

def resumo_pedido(request, item_pedido_id):
    item_pedido = get_object_or_404(ItemPedido, id=item_pedido_id)
    total = item_pedido.produto.preco + item_pedido.tamanho.preco_adicional
    total_final = total * item_pedido.quantidade

    return render(request, 'pedido/resumo_pedido.html', {
        'item_pedido': item_pedido,
        'total_final': total_final
    })
