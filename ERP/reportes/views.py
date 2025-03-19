# reportes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import FileResponse, HttpResponse
from .models import Reporte
from reportlab.pdfgen import canvas
from io import BytesIO
import openpyxl

@login_required
def lista_reportes(request):
    reportes = Reporte.objects.all().order_by('-fecha_generacion')
    return render(request, 'reportes/lista_reportes.html', {'reportes': reportes})

@login_required
def detalle_reporte(request, idReporte):
    reporte = get_object_or_404(Reporte, idReporte=idReporte)
    return render(request, 'reportes/detalle_reporte.html', {'reporte': reporte})

@login_required
def generar_reporte(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        rango_inicio = request.POST.get('rango_inicio')
        rango_fin = request.POST.get('rango_fin')
        try:
            if not tipo or not rango_inicio or not rango_fin:
                raise ValueError("Todos los campos son obligatorios.")
            if rango_inicio > rango_fin:
                raise ValueError("La fecha de inicio debe ser anterior a la fecha de fin.")
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

@login_required
def exportar_reporte_pdf(request, idReporte):
    reporte = get_object_or_404(Reporte, idReporte=idReporte)
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 750, f"Reporte #{reporte.idReporte}")
    p.drawString(100, 730, f"Tipo: {reporte.tipo.capitalize()}")
    p.drawString(100, 710, f"Fecha de Generación: {reporte.fecha_generacion.strftime('%d/%m/%Y %H:%M')}")
    p.drawString(100, 690, f"Generado por: {reporte.generado_por.username if reporte.generado_por else 'Usuario no disponible'}")
    # Agregar contenido del reporte
    p.drawString(100, 670, "Contenido:")
    y = 650
    for line in reporte.contenido.split('\n'):
        if y < 50:  # Nueva página si se acaba el espacio
            p.showPage()
            y = 750
        p.drawString(100, y, line[:80])  # Limitar longitud para evitar desbordamiento
        y -= 20
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"reporte_{reporte.idReporte}.pdf")

@login_required
def exportar_reporte_excel(request, idReporte):
    reporte = get_object_or_404(Reporte, idReporte=idReporte)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = f"Reporte_{reporte.idReporte}"
    ws.append(["ID Reporte", "Tipo", "Fecha Generación", "Usuario", "Rango Inicio", "Rango Fin", "Contenido"])
    ws.append([
        reporte.idReporte,
        reporte.tipo.capitalize(),
        reporte.fecha_generacion.strftime('%d/%m/%Y %H:%M'),
        reporte.generado_por.username if reporte.generado_por else 'Usuario no disponible',
        reporte.parametros.get('rango_inicio', 'N/A'),
        reporte.parametros.get('rango_fin', 'N/A'),
        reporte.contenido
    ])
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename=reporte_{reporte.idReporte}.xlsx'
    wb.save(response)
    return response

@login_required
def imprimir_reporte(request, idReporte):
    reporte = get_object_or_404(Reporte, idReporte=idReporte)
    return render(request, 'reportes/imprimir_reporte.html', {'reporte': reporte})