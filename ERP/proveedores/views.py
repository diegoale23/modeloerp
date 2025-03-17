from django.shortcuts import render, get_object_or_404
from .models import Proveedor

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/lista_proveedores.html', {'proveedores': proveedores})

def detalle_proveedor(request, idProveedor):
    proveedor = get_object_or_404(Proveedor, id=idProveedor)
    return render(request, 'proveedores/detalle_proveedor.html', {'proveedor': proveedor})

def crear_proveedor(request):
    if request.method == 'POST':
        # Procesar formulario
        pass
    return render(request, 'proveedores/crear_proveedor.html')
