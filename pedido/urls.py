from django.urls import path
from . import views

urlpatterns = [

    path('', views.listar_index, name='listar_index'),
    path('fazer-pedido/<int:produto_id>/', views.fazer_pedido, name='fazer_pedido'),
    path('resumo-pedido/<int:pedido_id>/', views.resumo_pedido, name='resumo_pedido'),

    path('fazer-pedido-personalizado/', views.fazer_pedido_personalizado, name='fazer_pedido_personalizado'),
    path('resumo-pedido-personalizado/<int:pedido_id>/', views.resumo_pedido_personalizado, name='resumo_pedido_personalizado'),

    path('meus-pedidos/', views.meus_pedidos, name='meus_pedidos'),
    path('listar-pedidos/', views.listar_pedidos, name='listar_pedidos'),
    path('pedido-confirmado/<int:pedido_id>/<str:tipo_pedido>/', views.pedido_confirmado, name='pedido_confirmado'),
    path('atualizar-status/<int:pedido_id>/<str:tipo_pedido>/', views.atualizar_status, name='atualizar_status'),

]
