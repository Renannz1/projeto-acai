from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm, UsuarioForm, UserLoginForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth import logout

from usuario.models import Usuario
from django.contrib.auth.decorators import login_required


@login_required
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/listar_usuarios.html', {'usuarios': usuarios})


@login_required
def editar_usuario(request, usuario_id):
    # Busca o objeto Usuario correspondente ao usuario_id no banco de dados.
    # Se não encontrar, retorna uma página 404 (não encontrado).
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    # Verifica se o usuário logado tem permissão para editar o perfil:
    # Se o usuário for um administrador (is_staff) ou o próprio dono do perfil (request.user == usuario.user).
    if request.user.is_staff or request.user == usuario.user:
        if request.method == 'POST':
            form = UsuarioForm(request.POST, instance=usuario)
            if form.is_valid():
                form.save()
                return redirect('listar_usuarios')
        else:
            form = UsuarioForm(instance=usuario)
        return render(request, 'usuario/editar_usuario.html', {'form': form})
    else:
        # se o usuário logado não tiver permissão, lança uma exceção de permissão negada.
        raise PermissionDenied


@login_required
def perfil_usuario(request):
    # pega o perfil do usuário logado
    usuario = request.user.usuario

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'usuario/perfil_usuario.html', {'form': form})



def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        usuario_form = UsuarioForm(request.POST)
        
        if user_form.is_valid() and usuario_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            

            usuario = usuario_form.save(commit=False)
            usuario.user = user
            usuario.save()

            login(request, user)
            return redirect('listar_usuarios')
    else:
        user_form = UserRegisterForm()
        usuario_form = UsuarioForm()

    return render(request, 'usuario/registrar_usuario.html', {
        'user_form': user_form,
        'usuario_form': usuario_form
    })



def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('listar_usuarios')
    else:
        # Se o método não for POST, cria uma instância vazia do formulário de login
        form = UserLoginForm()

    return render(request, 'usuario/login_usuario.html', {'form': form})



def custom_logout(request):
    logout(request)
    return redirect('listar_usuarios')