from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_index, name='listar_index'),
    path('fazer-pedido/<int:produto_id>/', views.fazer_pedido, name='fazer_pedido'),
    path('resumo-pedido/<int:pedido_id>/', views.resumo_pedido, name='resumo_pedido'),
]
