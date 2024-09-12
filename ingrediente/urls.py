from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_ingredientes, name='listar_ingredientes'),
    path('adicionar/', views.adicionar_ingrediente, name='adicionar_ingrediente'),
    path('editar/<int:ingrediente_id>/', views.editar_ingrediente, name='editar_ingrediente'),
    path('remover/<int:ingrediente_id>/', views.remover_ingrediente, name='remover_ingrediente'),
]
