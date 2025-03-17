from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_reportes, name='lista_reportes'),  # Listar todos los reportes
    path('<int:idReporte>/', views.detalle_reporte, name='detalle_reporte'),  # Detalle de un reporte específico
    path('generar/', views.generar_reporte, name='generar_reporte'),  # Generar un nuevo reporte
]
