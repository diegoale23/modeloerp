from django.shortcuts import render, get_object_or_404
from .models import RegistroFinanciero, InformeFinanciero

def lista_registros(request):
    registros = RegistroFinanciero.objects.all()
    return render(request, 'gestion_financiera/lista_registros.html', {'registros': registros})

def detalle_registro(request, idRegistro):
    registro = get_object_or_404(RegistroFinanciero, id=idRegistro)
    return render(request, 'gestion_financiera/detalle_registro.html', {'registro': registro})

def generar_informe(request):
    if request.method == 'POST':
        # Procesar parámetros para generar el informe
        pass
    return render(request, 'gestion_financiera/generar_informe.html')
