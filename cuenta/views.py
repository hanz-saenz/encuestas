from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .models import Perfil
from .forms import PerfilForm
# Create your views here.

def regitro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_encuestas')
        else:
            return render(request, 'cuenta/registro.html', {'form': form, 'error': 'Formulario inválido'})
    else:
        form = UserCreationForm()


    return render(request, 'cuenta/registro.html', {'form': form})


class LoginUsuarioView(LoginView):
    template_name = 'cuenta/login.html'


def logout_usuario(request):
    logout(request)  
    return redirect('login')


def perfil(request):

    perfil = Perfil.objects.get(user=request.user)
    print(perfil)
    
    return render(request, 'cuenta/perfil.html', {'perfil': perfil})

def editar_perfil(request, id_usuario):
    # perfil = Perfil.objects.get(user_id=id_usuario)

    perfil = get_object_or_404(Perfil, id=id_usuario)
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'cuenta/editar_perfil.html', {'form': form})