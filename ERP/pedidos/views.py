from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Pedido, DetallePedido
from usuarios.models import Usuario
from inventario.models import Producto
from django.db import transaction
from django.core.exceptions import ValidationError

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
    clientes = Usuario.objects.filter(rol='cliente')  # Solo clientes
    productos = Producto.objects.all()  # Todos los productos disponibles

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        productos_seleccionados = request.POST.getlist('productos')  # Lista de IDs de productos
        cantidades = request.POST.getlist('cantidades')  # Lista de cantidades

        # Diccionario para almacenar errores específicos
        errores = {}

        # Validar cliente
        if not cliente_id:
            errores['cliente'] = 'Debes seleccionar un cliente.'
        else:
            try:
                cliente = get_object_or_404(Usuario, idUsuario=cliente_id)
            except:
                errores['cliente'] = 'Cliente no válido.'

        # Validar productos y cantidades
        if not productos_seleccionados or not cantidades:
            errores['productos'] = 'Debes seleccionar al menos un producto con cantidad mayor a 0.'
        elif len(productos_seleccionados) != len(cantidades):
            errores['productos'] = 'Error en la cantidad de productos seleccionados.'

        detalles_validos = []
        total = 0
        for prod_id, cantidad in zip(productos_seleccionados, cantidades):
            try:
                cantidad = int(cantidad)
                if cantidad <= 0:
                    continue  # Saltar si la cantidad es 0 o negativa

                producto = get_object_or_404(Producto, idProducto=prod_id)
                if producto.stock < cantidad:
                    errores[f'producto_{prod_id}'] = f'Stock insuficiente para {producto.nombre} (disponible: {producto.stock}).'
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

        # Si no hay detalles válidos, agregar error
        if not detalles_validos:
            errores['productos'] = 'Debes seleccionar al menos un producto con cantidad válida.'

        # Si hay errores, devolver el formulario con ellos
        if errores:
            return render(request, 'pedidos/crear_pedido.html', {
                'clientes': clientes,
                'productos': productos,
                'errores': errores,
                'valores': request.POST  # Para mantener los valores ingresados
            })

        # Si todo está validado, proceder a guardar
        try:
            with transaction.atomic():
                pedido = Pedido(
                    cliente=cliente,
                    total=total
                )
                pedido.save()

                for detalle in detalles_validos:
                    DetallePedido.objects.create(
                        pedido=pedido,
                        producto=detalle['producto'],
                        cantidad=detalle['cantidad'],
                        subtotal=detalle['subtotal']
                    )
                    # Actualizar stock
                    detalle['producto'].actualizar_stock(-detalle['cantidad'])

                return redirect('lista_pedidos')

        except Exception as e:
            return render(request, 'pedidos/crear_pedido.html', {
                'clientes': clientes,
                'productos': productos,
                'errores': {'general': f'Error al guardar el pedido: {str(e)}'},
                'valores': request.POST
            })

    return render(request, 'pedidos/crear_pedido.html', {
        'clientes': clientes,
        'productos': productos
    })