from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Usuario

@login_required
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

@login_required
def detalle_usuario(request, idUsuario):
    usuario = get_object_or_404(Usuario, id=idUsuario)
    return render(request, 'usuarios/detalle_usuario.html', {'usuario': usuario})

@login_required
def crear_usuario(request):
    if request.method == 'POST':
        # Procesar formulario
        pass
    return render(request, 'usuarios/crear_usuario.html')
