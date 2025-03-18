# reportes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Reporte

@login_required
def lista_reportes(request):
    """
    Muestra la lista de reportes generados.
    """
    reportes = Reporte.objects.all().order_by('-fecha_generacion')
    return render(request, 'reportes/lista_reportes.html', {'reportes': reportes})

@login_required
def detalle_reporte(request, idReporte):
    """
    Muestra los detalles de un reporte específico.
    """
    reporte = get_object_or_404(Reporte, idReporte=idReporte)
    return render(request, 'reportes/detalle_reporte.html', {'reporte': reporte})

@login_required
def generar_reporte(request):
    """
    Genera un nuevo reporte basado en parámetros proporcionados por el usuario.
    """
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        rango_inicio = request.POST.get('rango_inicio')
        rango_fin = request.POST.get('rango_fin')

        try:
            # Validar parámetros básicos
            if not tipo or not rango_inicio or not rango_fin:
                raise ValueError("Todos los campos son obligatorios.")
            if rango_inicio > rango_fin:
                raise ValueError("La fecha de inicio debe ser anterior a la fecha de fin.")

            # Crear y generar el reporte
            reporte = Reporte()
            reporte.generar(
                tipo=tipo,
                usuario=request.user,
                rango_inicio=rango_inicio,
                rango_fin=rango_fin
            )
            messages.success(request, f"Reporte {tipo.capitalize()} generado exitosamente.")
            return redirect('detalle_reporte', idReporte=reporte.idReporte)
        except ValueError as e:
            messages.error(request, f"Error al generar el reporte: {str(e)}")
            return render(request, 'reportes/generar_reporte.html', {
                'tipo': tipo,
                'rango_inicio': rango_inicio,
                'rango_fin': rango_fin
            })
        except Exception as e:
            messages.error(request, f"Error inesperado: {str(e)}")
            return render(request, 'reportes/generar_reporte.html', {
                'tipo': tipo,
                'rango_inicio': rango_inicio,
                'rango_fin': rango_fin
            })

    return render(request, 'reportes/generar_reporte.html')