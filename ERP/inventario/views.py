from django.shortcuts import render, get_object_or_404
from .models import Producto, MovimientoInventario

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/lista_productos.html', {'productos': productos})

def detalle_producto(request, idProducto):
    producto = get_object_or_404(Producto, id=idProducto)
    return render(request, 'inventario/detalle_producto.html', {'producto': producto})

def registrar_movimiento(request):
    if request.method == 'POST':
        # Procesar formulario para movimiento de inventario
        pass
    return render(request, 'inventario/registrar_movimiento.html')
