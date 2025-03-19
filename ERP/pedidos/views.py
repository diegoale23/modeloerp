from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Pedido, DetallePedido
from usuarios.models import Usuario
from inventario.models import Producto
from django.db import transaction
from django.core.exceptions import ValidationError

def es_superusuario(user):
    return user.is_superuser

@login_required
def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/lista_pedidos.html', {'pedidos': pedidos})

@login_required
def detalle_pedido(request, idPedido):
    pedido = get_object_or_404(Pedido, idPedido=idPedido)
    return render(request, 'pedidos/detalle_pedido.html', {'pedido': pedido})

@login_required
def crear_pedido(request):
    # [Tu código existente de crear_pedido, sin cambios]
    clientes = Usuario.objects.filter(rol='cliente')
    productos = Producto.objects.all()
    if request.method == 'POST':
        # [Lógica existente]
        pass
    return render(request, 'pedidos/crear_pedido.html', {'clientes': clientes, 'productos': productos})

@login_required
def modificar_pedido(request, idPedido):
    pedido = get_object_or_404(Pedido, idPedido=idPedido)
    clientes = Usuario.objects.filter(rol='cliente')
    productos = Producto.objects.all()

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        estado = request.POST.get('estado')  # Nuevo: obtenemos el estado
        productos_seleccionados = request.POST.getlist('productos')
        cantidades = request.POST.getlist('cantidades')
        errores = {}

        if not cliente_id:
            errores['cliente'] = 'Debes seleccionar un cliente.'
        else:
            cliente = get_object_or_404(Usuario, idUsuario=cliente_id)

        if estado not in ['pendiente', 'procesado']:
            errores['estado'] = 'Estado inválido.'

        # Lógica existente para productos y cantidades
        detalles_validos = []
        total = 0
        for prod_id, cantidad in zip(productos_seleccionados, cantidades):
            try:
                cantidad = int(cantidad)
                if cantidad <= 0:
                    continue
                producto = get_object_or_404(Producto, idProducto=prod_id)
                if producto.stock < cantidad:
                    errores[f'producto_{prod_id}'] = f'Stock insuficiente para {producto.nombre}.'
                else:
                    subtotal = producto.precio * cantidad
                    total += subtotal
                    detalles_validos.append({
                        'producto': producto,
                        'cantidad': cantidad,
                        'subtotal': subtotal
                    })
            except ValueError:
                errores[f'producto_{prod_id}'] = 'Cantidad inválida.'

        if not detalles_validos:
            errores['productos'] = 'Debes seleccionar al menos un producto con cantidad válida.'

        if errores:
            return render(request, 'pedidos/modificar_pedido.html', {
                'pedido': pedido, 'clientes': clientes, 'productos': productos,
                'errores': errores, 'valores': request.POST
            })

        try:
            with transaction.atomic():
                for detalle in pedido.detallepedido_set.all():
                    detalle.producto.actualizar_stock(detalle.cantidad)
                    detalle.delete()

                pedido.cliente = cliente
                pedido.estado = estado  # Nuevo: actualizamos el estado
                pedido.total = total
                pedido.save()

                for detalle in detalles_validos:
                    DetallePedido.objects.create(
                        pedido=pedido,
                        producto=detalle['producto'],
                        cantidad=detalle['cantidad'],
                        subtotal=detalle['subtotal']
                    )
                    detalle['producto'].actualizar_stock(-detalle['cantidad'])

                return redirect('lista_pedidos')
        except Exception as e:
            return render(request, 'pedidos/modificar_pedido.html', {
                'pedido': pedido, 'clientes': clientes, 'productos': productos,
                'errores': {'general': f'Error al modificar el pedido: {str(e)}'},
                'valores': request.POST
            })

    return render(request, 'pedidos/modificar_pedido.html', {
        'pedido': pedido, 'clientes': clientes, 'productos': productos
    })

@login_required
def eliminar_pedido(request, idPedido):
    pedido = get_object_or_404(Pedido, idPedido=idPedido)
    if pedido.estado == 'procesado':
        messages.error(request, f"No puedes eliminar el pedido #{idPedido} porque ya está procesado.")
        return redirect('lista_pedidos')
    
    if request.method == 'POST':
        try:
            with transaction.atomic():
                for detalle in pedido.detallepedido_set.all():
                    detalle.producto.actualizar_stock(detalle.cantidad)  # Devolver stock
                pedido.delete()
            messages.success(request, f"Pedido #{idPedido} eliminado exitosamente.")
        except Exception as e:
            messages.error(request, f"Error al eliminar el pedido: {str(e)}")
        return redirect('lista_pedidos')
    return redirect('lista_pedidos')