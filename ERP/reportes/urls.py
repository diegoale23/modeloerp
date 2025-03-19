from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_reportes, name='lista_reportes'),
    path('<int:idReporte>/', views.detalle_reporte, name='detalle_reporte'),
    path('generar/', views.generar_reporte, name='generar_reporte'),
    path('exportar/pdf/<int:idReporte>/', views.exportar_reporte_pdf, name='exportar_reporte_pdf'),
    path('exportar/excel/<int:idReporte>/', views.exportar_reporte_excel, name='exportar_reporte_excel'),
    path('imprimir/<int:idReporte>/', views.imprimir_reporte, name='imprimir_reporte'),
]