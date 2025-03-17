from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Proveedor

# Solo superusuarios
def es_superusuario(user):
    return user.is_superuser

@login_required
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/lista_proveedores.html', {'proveedores': proveedores})

@login_required
def detalle_proveedor(request, idProveedor):
    proveedor = get_object_or_404(Proveedor, idProveedor=idProveedor)
    return render(request, 'proveedores/detalle_proveedor.html', {'proveedor': proveedor})

@login_required
def crear_proveedor(request):
    if request.method == 'POST':
        try:
            proveedor = Proveedor(
                nombre=request.POST.get('nombre'),
                contacto=request.POST.get('contacto'),
                direccion=request.POST.get('direccion'),
                telefono=request.POST.get('telefono'),
                email=request.POST.get('email'),
            )
            proveedor.save()
            return redirect('lista_proveedores')
        except Exception as e:
            return render(request, 'proveedores/crear_proveedor.html', {
                'error': f'Error al crear proveedor: {str(e)}'
            })
    return render(request, 'proveedores/crear_proveedor.html')

@login_required
def modificar_proveedor(request, idProveedor):
    proveedor = get_object_or_404(Proveedor, idProveedor=idProveedor)
    if request.method == 'POST':
        try:
            proveedor.nombre = request.POST.get('nombre')
            proveedor.contacto = request.POST.get('contacto')
            proveedor.direccion = request.POST.get('direccion')
            proveedor.telefono = request.POST.get('telefono')
            proveedor.email = request.POST.get('email')
            proveedor.save()
            return redirect('lista_proveedores')
        except Exception as e:
            return render(request, 'proveedores/modificar_proveedor.html', {
                'proveedor': proveedor,
                'error': f'Error al modificar proveedor: {str(e)}'
            })
    return render(request, 'proveedores/modificar_proveedor.html', {'proveedor': proveedor})

@login_required
@user_passes_test(es_superusuario, login_url='/proveedores/')
def eliminar_proveedor(request, idProveedor):
    proveedor = get_object_or_404(Proveedor, idProveedor=idProveedor)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('lista_proveedores')
    return render(request, 'proveedores/eliminar_proveedor.html', {'proveedor': proveedor})