from venv import logger
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from usuario.forms import CadastroForm, LoginForm, ExtendedCadastroForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def logout_user(request):
    logout(request)
    return redirect('inicio')

@login_required
def paineldousuario(request):
    usuario = request.user
    dados_usuario ={}
    if usuario.is_authenticated:
        dados_usuario = {
           'id': usuario.id,
            'username': usuario.username,
            'email': usuario.email,
        }
    return render(request, 'galeria/paineldousuario.html', {'usuario': dados_usuario} )

def cadastro_user(request):
    if request.method == 'POST':
        form = ExtendedCadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                logger.info(f'Usuário (a) {user.username} autenticado com sucesso após o cadastro')
                return redirect('paineldousuario')
            else:
                logger.error('Erro !!! Usuário não autenticado após o cadastro')
    else:
        form = CadastroForm()
    return render(request, 'galeria/cadastro.html', {'form': form})

def fazer_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('paineldousuario')  
    else:
        form = LoginForm()
    return render(request, 'galeria/login.html', {'form': form})

@login_required  
def gerenciar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        novo_email = request.POST.get('email')
        if novo_email != usuario.email:
            usuario.email = novo_email
            usuario.save()
            messages.success(request, 'Perfil atualizado com sucesso')
        else:
            messages.info(request, 'Nenhuma alteração foi feita')
    return render(request, 'galeria/gerenciar_perfil.html', {'usuario': usuario})