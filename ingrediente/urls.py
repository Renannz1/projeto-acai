from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_ingredientes, name='listar_ingredientes'),
    path('adicionar/', views.adicionar_ingrediente, name='adicionar_ingrediente'),
    path('editar/<int:ingrediente_id>/', views.editar_ingrediente, name='editar_ingrediente'),
    path('remover/<int:ingrediente_id>/', views.remover_ingrediente, name='remover_ingrediente'),

    path('tamanho/', views.listar_tamanhos, name='listar_tamanhos'),
    path('tamanho/adicionar/', views.adicionar_tamanho, name='adicionar_tamanho'),
    path('tamanho/editar/<int:tamanho_id>/', views.editar_tamanho, name='editar_tamanho'),
    path('tamanho/remover/<int:tamanho_id>/', views.remover_tamanho, name='remover_tamanho'),
]

