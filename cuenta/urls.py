from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('registro', regitro_usuario, name='registro'),
    path('login', LoginUsuarioView.as_view(), name='login'),
    path('logout', logout_usuario, name='logout'),
    path('perfil', perfil, name='perfil'),
    path('perfil/editar/<int:id_usuario>', editar_perfil, name='editar_perfil'),
    
]
