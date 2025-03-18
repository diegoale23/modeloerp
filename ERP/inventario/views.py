from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from .models import Producto, MovimientoInventario

# Función para verificar si el usuario es superusuario
def es_superusuario(user):
    return user.is_superuser

@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/lista_productos.html', {'productos': productos})

@login_required
def detalle_producto(request, idProducto):
    producto = get_object_or_404(Producto, idProducto=idProducto)
    return render(request, 'inventario/detalle_producto.html', {'producto': producto})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            descripcion = request.POST.get('descripcion', '')
            precio = request.POST.get('precio')
            stock = request.POST.get('stock')

            # Validaciones básicas
            if not nombre or not precio or not stock:
                return render(request, 'inventario/crear_producto.html', {
                    'error': 'Todos los campos obligatorios deben estar completos.',
                    'valores': request.POST
                })

            producto = Producto(
                nombre=nombre,
                descripcion=descripcion,
                precio=float(precio),  # Convertimos a float para DecimalField
                stock=int(stock)       # Convertimos a int
            )
            producto.save()
            return redirect('lista_productos')

        except ValueError as e:
            return render(request, 'inventario/crear_producto.html', {  # Corregido: 'inventario/crear_producto.html'
                'error': f'Error en los datos ingresados: {str(e)}',
                'valores': request.POST
            })
        except Exception as e:
            return render(request, 'inventario/crear_producto.html', {  # Corregido: 'inventario/crear_producto.html'
                'error': f'Error al guardar el producto: {str(e)}',
                'valores': request.POST
            })
    return render(request, 'inventario/crear_producto.html')

@login_required
def registrar_movimiento(request):
    productos = Producto.objects.all()

    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        tipo = request.POST.get('tipo')
        cantidad = request.POST.get('cantidad')
        descripcion = request.POST.get('descripcion', '')

        errores = {}

        # Validar producto
        if not producto_id:
            errores['producto'] = 'Debes seleccionar un producto.'
        else:
            producto = get_object_or_404(Producto, idProducto=producto_id)

        # Validar tipo
        if tipo not in ['entrada', 'salida']:
            errores['tipo'] = 'Tipo de movimiento no válido.'

        # Validar cantidad
        try:
            cantidad = int(cantidad)
            if cantidad <= 0:
                errores['cantidad'] = 'La cantidad debe ser mayor a 0.'
            elif tipo == 'salida' and producto and cantidad > producto.stock:
                errores['cantidad'] = f'Stock insuficiente (disponible: {producto.stock}).'
        except (ValueError, TypeError):
            errores['cantidad'] = 'La cantidad debe ser un número válido.'

        if errores:
            return render(request, 'inventario/registrar_movimiento.html', {
                'productos': productos,
                'errores': errores,
                'valores': request.POST
            })

        try:
            with transaction.atomic():
                movimiento = MovimientoInventario(
                    producto=producto,
                    tipo=tipo,
                    cantidad=cantidad,
                    descripcion=descripcion
                )
                movimiento.aplicar_movimiento()
                return redirect('lista_productos')

        except ValueError as e:
            errores['general'] = str(e)
            return render(request, 'inventario/registrar_movimiento.html', {
                'productos': productos,
                'errores': errores,
                'valores': request.POST
            })
        except Exception as e:
            errores['general'] = f'Error al registrar el movimiento: {str(e)}'
            return render(request, 'inventario/registrar_movimiento.html', {
                'productos': productos,
                'errores': errores,
                'valores': request.POST
            })

    return render(request, 'inventario/registrar_movimiento.html', {
        'productos': productos
    })

@login_required
def editar_producto(request, idProducto):
    producto = get_object_or_404(Producto, idProducto=idProducto)
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            descripcion = request.POST.get('descripcion', '')
            precio = request.POST.get('precio')
            stock = request.POST.get('stock')

            # Validaciones
            if not nombre or not precio or not stock:
                return render(request, 'inventario/editar_producto.html', {
                    'producto': producto,
                    'error': 'Todos los campos obligatorios deben estar completos.',
                    'valores': request.POST
                })

            producto.nombre = nombre
            producto.descripcion = descripcion
            producto.precio = float(precio)
            producto.stock = int(stock)
            producto.save()
            return redirect('detalle_producto', idProducto=producto.idProducto)

        except ValueError as e:
            return render(request, 'inventario/editar_producto.html', {
                'producto': producto,
                'error': f'Error en los datos ingresados: {str(e)}',
                'valores': request.POST
            })
        except Exception as e:
            return render(request, 'inventario/editar_producto.html', {
                'producto': producto,
                'error': f'Error al editar el producto: {str(e)}',
                'valores': request.POST
            })
    return render(request, 'inventario/editar_producto.html', {'producto': producto})

@login_required
#@user_passes_test(es_superusuario, login_url='/inventario/')
def eliminar_producto(request, idProducto):
    producto = get_object_or_404(Producto, idProducto=idProducto)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'inventario/eliminar_producto.html', {'producto': producto})