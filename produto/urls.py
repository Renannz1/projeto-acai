from django.urls import path
from . import views

urlpatterns = [
#   path('', views.listar_produtos, name='listar_produtos'),
#   path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
#   path('editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
#   path('remover/<int:produto_id>/', views.remover_produto, name='remover_produto'),

    path('listar', views.ProdutoListView.as_view(), name= 'listar_produtos'),
    path('adicionar/', views.ProdutoCreateView.as_view(), name= 'adicionar_produto'),
    path('editar/<int:pk>', views.ProdtuoUpdateView.as_view(), name= 'editar_produto'),
    path('remover/<int:pk>', views.ProdutoDeleteView.as_view(), name= 'remover_produto'),

]
