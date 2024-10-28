from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Produto
from .forms import ProdutoForm

# def listar_produtos(request):
#     produtos = Produto.objects.all()
#     return render(request, 'produto/listar_produtos.html', {'produtos': produtos})

# def adicionar_produto(request):
#     if request.method == 'POST':
#         form = ProdutoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('listar_produtos')
#     else:
#         form = ProdutoForm()
#     return render(request, 'produto/adicionar_produto.html', {'form': form})

# def editar_produto(request, produto_id):
#     produto = get_object_or_404(Produto, id=produto_id)
#     if request.method == 'POST':
#         form = ProdutoForm(request.POST, request.FILES, instance=produto)
#         if form.is_valid():
#             form.save()
#             return redirect('listar_produtos')
#     else:
#         form = ProdutoForm(instance=produto)
#     return render(request, 'produto/editar_produto.html', {'form': form})

def remover_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')
    return render(request, 'produto/remover_produto.html', {'produto': produto})



## USANDO CLASSES GENERICAS DO DJANGO



class ProdutoCreateView(CreateView):
    model = Produto
    template_name = "produto/adicionar_produto.html"
    fields = '__all__'
    success_url = 'listar_produtos'

class ProdutoListView(ListView):
    model = Produto
    template_name = "produto/listar_produtos.html"
    context_object_name = 'produtos'

class ProdtuoUpdateView(UpdateView):
    model = Produto
    template_name = "produto/editar_produto.html"
    fields = ['nome', 'preco', 'sabor', 'acompanhamentos', 'imagem']
    success_url = reverse_lazy('listar_produtos')



