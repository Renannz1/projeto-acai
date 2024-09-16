from django.urls import path
from . import views

urlpatterns = [
    # lista todos os ingredientes
    path('ingredientes/', views.listar_ingredientes, name='listar_ingredientes'),

    # acompanhamentos
    path('acompanhamentos/adicionar/', views.adicionar_acompanhamento, name='adicionar_acompanhamento'),
    path('acompanhamentos/editar/<int:acompanhamento_id>/', views.editar_acompanhamento, name='editar_acompanhamento'),
    path('acompanhamentos/remover/<int:acompanhamento_id>/', views.remover_acompanhamento, name='remover_acompanhamento'),

    # sabores
    path('sabores/adicionar/', views.adicionar_sabor, name='adicionar_sabor'),
    path('sabores/editar/<int:sabor_id>/', views.editar_sabor, name='editar_sabor'),
    path('sabores/remover/<int:sabor_id>/', views.remover_sabor, name='remover_sabor'),

    # tamanhos
    path('tamanhos/adicionar/', views.adicionar_tamanho, name='adicionar_tamanho'),
    path('tamanhos/editar/<int:tamanho_id>/', views.editar_tamanho, name='editar_tamanho'),
    path('tamanhos/remover/<int:tamanho_id>/', views.remover_tamanho, name='remover_tamanho'),
]
