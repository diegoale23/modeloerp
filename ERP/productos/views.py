from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto

def lista_productos(request):
    """
    Muestra la lista de todos los productos disponibles en el inventario.
    """
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def detalle_producto(request, idProducto):
    """
    Muestra los detalles de un producto específico.
    """
    producto = get_object_or_404(Producto, id=idProducto)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})

def crear_producto(request):
    """
    Permite crear un nuevo producto.
    """
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')

        producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock
        )
        producto.save()
        return redirect('lista_productos')
    
    return render(request, 'productos/crear_producto.html')

def editar_producto(request, idProducto):
    """
    Permite editar la información de un producto existente.
    """
    producto = get_object_or_404(Producto, id=idProducto)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.save()
        return redirect('detalle_producto', idProducto=producto.id)

    return render(request, 'productos/editar_producto.html', {'producto': producto})

def eliminar_producto(request, idProducto):
    """
    Permite eliminar un producto del inventario.
    """
    producto = get_object_or_404(Producto, id=idProducto)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')

    return render(request, 'productos/eliminar_producto.html', {'producto': producto})
