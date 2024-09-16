from . import views
from django.urls import path
from .views import custom_logout, register, login_view


urlpatterns = [
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.custom_logout, name='logout'),
]