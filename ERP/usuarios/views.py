from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Usuario

# Solo superusuarios
def es_superusuario(user):
    return user.is_superuser

@login_required
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

@login_required
def detalle_usuario(request, idUsuario):
    usuario = get_object_or_404(Usuario, idUsuario=idUsuario)
    return render(request, 'usuarios/detalle_usuario.html', {'usuario': usuario})

@login_required
def crear_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        try:
            usuario = Usuario(
                nombre=nombre,
                apellido=apellido,
                email=email,
                username=email,
                rol='cliente'
            )
            usuario.set_password('default123')
            usuario.save()
            return redirect('lista_usuarios')
        except Exception as e:
            return render(request, 'usuarios/crear_usuario.html', {
                'error': f'Error al crear usuario: {str(e)}'
            })
    return render(request, 'usuarios/crear_usuario.html')

@login_required
def modificar_usuario(request, idUsuario):
    usuario = get_object_or_404(Usuario, idUsuario=idUsuario)
    if request.method == 'POST':
        try:
            usuario.nombre = request.POST.get('nombre')
            usuario.apellido = request.POST.get('apellido')
            usuario.email = request.POST.get('email')
            usuario.username = usuario.email  # Actualizar username si email cambia
            usuario.save()
            return redirect('lista_usuarios')
        except Exception as e:
            return render(request, 'usuarios/modificar_usuario.html', {
                'usuario': usuario,
                'error': f'Error al modificar usuario: {str(e)}'
            })
    return render(request, 'usuarios/modificar_usuario.html', {'usuario': usuario})

@login_required
#@user_passes_test(es_superusuario, login_url='/usuarios/')  # Solo superusuarios pueden eliminar
def eliminar_usuario(request, idUsuario):
    usuario = get_object_or_404(Usuario, idUsuario=idUsuario)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'usuarios/eliminar_usuario.html', {'usuario': usuario})