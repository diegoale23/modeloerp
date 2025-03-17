from django.urls import path
from . import views

urlpatterns = [
    path('registros/', views.lista_registros, name='lista_registros'),  # Listar todos los registros financieros
    path('registros/<int:idRegistro>/', views.detalle_registro, name='detalle_registro'),  # Detalle de un registro financiero específico
    path('informes/generar/', views.generar_informe, name='generar_informe'),  # Generar un nuevo informe financiero
]
