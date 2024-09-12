
from django.urls import path
from . import views  

urlpatterns = [
    path('pedido/acai-pronto/', views.fazer_pedido_acai_pronto, name='pedido_acai_pronto'),
    path('pedido/acai-personalizado/', views.fazer_pedido_acai_personalizado, name='pedido_acai_personalizado'),
    path('resumo-pedido-pronto/<int:pedido_id>/', views.resumo_pedido_pronto, name='resumo_pedido_pronto'),
    path('resumo-pedido-personalizado/<int:pedido_id>/', views.resumo_pedido_personalizado, name='resumo_pedido_personalizado'),
]
