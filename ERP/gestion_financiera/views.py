# gestion_financiera/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import RegistroFinanciero, InformeFinanciero
from usuarios.models import Usuario  # Modelo de clientes

@login_required
def lista_registros(request):
    registros = RegistroFinanciero.objects.all().order_by('-fecha')
    return render(request, 'gestion_financiera/lista_registros.html', {'registros': registros})

@login_required
def detalle_registro(request, idRegistro):
    registro = get_object_or_404(RegistroFinanciero, idRegistro=idRegistro)
    return render(request, 'gestion_financiera/detalle_registro.html', {'registro': registro})

@login_required
def crear_registro(request):
    clientes = Usuario.objects.filter(rol='cliente')  # Solo clientes
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        monto = request.POST.get('monto')
        descripcion = request.POST.get('descripcion', '')
        cliente_id = request.POST.get('cliente')

        try:
            monto = float(monto)
            if monto <= 0:
                raise ValueError("El monto debe ser mayor a 0.")
            if not cliente_id:
                raise ValueError("Debes seleccionar un cliente.")
            cliente = get_object_or_404(Usuario, idUsuario=cliente_id)
            registro = RegistroFinanciero(
                tipo=tipo,
                monto=monto,
                descripcion=descripcion,
                usuario=cliente  # Asignamos el cliente seleccionado
            )
            registro.save()
            messages.success(request, "Registro financiero creado exitosamente.")
            return redirect('lista_registros')
        except ValueError as e:
            messages.error(request, f"Error al crear el registro: {str(e)}")
            return render(request, 'gestion_financiera/crear_registro.html', {
                'clientes': clientes,
                'tipo': tipo,
                'monto': monto,
                'descripcion': descripcion,
                'cliente_id': cliente_id
            })
        except Exception as e:
            messages.error(request, f"Error inesperado: {str(e)}")
            return render(request, 'gestion_financiera/crear_registro.html', {
                'clientes': clientes,
                'tipo': tipo,
                'monto': monto,
                'descripcion': descripcion,
                'cliente_id': cliente_id
            })

    return render(request, 'gestion_financiera/crear_registro.html', {'clientes': clientes})

@login_required
def editar_registro(request, idRegistro):
    registro = get_object_or_404(RegistroFinanciero, idRegistro=idRegistro)
    clientes = Usuario.objects.filter(rol='cliente')
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        monto = request.POST.get('monto')
        descripcion = request.POST.get('descripcion', '')
        cliente_id = request.POST.get('cliente')

        try:
            monto = float(monto)
            if monto <= 0:
                raise ValueError("El monto debe ser mayor a 0.")
            if not cliente_id:
                raise ValueError("Debes seleccionar un cliente.")
            cliente = get_object_or_404(Usuario, idUsuario=cliente_id)
            registro.tipo = tipo
            registro.monto = monto
            registro.descripcion = descripcion
            registro.usuario = cliente  # Actualizamos el cliente
            registro.save()
            messages.success(request, "Registro financiero actualizado exitosamente.")
            return redirect('lista_registros')
        except ValueError as e:
            messages.error(request, f"Error al actualizar el registro: {str(e)}")
            return render(request, 'gestion_financiera/editar_registro.html', {
                'registro': registro,
                'clientes': clientes,
                'tipo': tipo,
                'monto': monto,
                'descripcion': descripcion,
                'cliente_id': cliente_id
            })
        except Exception as e:
            messages.error(request, f"Error inesperado: {str(e)}")
            return render(request, 'gestion_financiera/editar_registro.html', {
                'registro': registro,
                'clientes': clientes,
                'tipo': tipo,
                'monto': monto,
                'descripcion': descripcion,
                'cliente_id': cliente_id
            })

    return render(request, 'gestion_financiera/editar_registro.html', {
        'registro': registro,
        'clientes': clientes
    })

@login_required
def eliminar_registro(request, idRegistro):
    registro = get_object_or_404(RegistroFinanciero, idRegistro=idRegistro)
    if request.method == 'POST':
        try:
            registro.delete()
            messages.success(request, f"Registro #{idRegistro} eliminado exitosamente.")
        except Exception as e:
            messages.error(request, f"Error al eliminar el registro: {str(e)}")
        return redirect('lista_registros')
    return redirect('lista_registros')

@login_required
def generar_informe(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        rango_inicio = request.POST.get('rango_inicio')
        rango_fin = request.POST.get('rango_fin')

        try:
            if not tipo or not rango_inicio or not rango_fin:
                raise ValueError("Todos los campos son obligatorios.")
            if rango_inicio > rango_fin:
                raise ValueError("La fecha de inicio debe ser anterior a la fecha de fin.")
            if tipo not in ['totales', 'ingreso', 'gasto']:
                raise ValueError("Tipo de informe inválido.")

            informe = InformeFinanciero(
                rango_inicio=rango_inicio,
                rango_fin=rango_fin,
                generado_por=request.user
            )
            informe.generar_informe(tipo=tipo)  # Pasar el tipo al método
            messages.success(request, "Informe generado exitosamente.")
            return redirect('detalle_informe', idInforme=informe.idInforme)
        except ValueError as e:
            messages.error(request, f"Error al generar el informe: {str(e)}")
            return render(request, 'gestion_financiera/generar_informe.html', {
                'tipo': tipo,
                'rango_inicio': rango_inicio,
                'rango_fin': rango_fin
            })
        except Exception as e:
            messages.error(request, f"Error inesperado: {str(e)}")
            return render(request, 'gestion_financiera/generar_informe.html', {
                'tipo': tipo,
                'rango_inicio': rango_inicio,
                'rango_fin': rango_fin
            })

    return render(request, 'gestion_financiera/generar_informe.html')

@login_required
def detalle_informe(request, idInforme):
    informe = get_object_or_404(InformeFinanciero, idInforme=idInforme)
    return render(request, 'gestion_financiera/detalle_informe.html', {'informe': informe})