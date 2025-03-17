from django.shortcuts import render, get_object_or_404
from .models import Reporte

def lista_reportes(request):
    """
    Muestra la lista de reportes generados.
    """
    reportes = Reporte.objects.all()
    return render(request, 'reportes/lista_reportes.html', {'reportes': reportes})

def detalle_reporte(request, idReporte):
    """
    Muestra los detalles de un reporte específico.
    """
    reporte = get_object_or_404(Reporte, id=idReporte)
    return render(request, 'reportes/detalle_reporte.html', {'reporte': reporte})

def generar_reporte(request):
    """
    Genera un nuevo reporte basado en parámetros proporcionados por el usuario.
    """
    if request.method == 'POST':
        # Procesar los parámetros del formulario (e.g., rango de fechas)
        rango_inicio = request.POST.get('rango_inicio')
        rango_fin = request.POST.get('rango_fin')

        # Crear un nuevo reporte
        reporte = Reporte(
            rango_inicio=rango_inicio,
            rango_fin=rango_fin,
            generado_por=request.user
        )
        reporte.generar_informe()  # Llama al método que genera el contenido
        return redirect('detalle_reporte', idReporte=reporte.id)

    return render(request, 'reportes/generar_reporte.html')
