from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_registros, name='lista_registros'),
    path('detalle/<int:idRegistro>/', views.detalle_registro, name='detalle_registro'),
    path('crear/', views.crear_registro, name='crear_registro'),
    path('editar/<int:idRegistro>/', views.editar_registro, name='editar_registro'),
    path('eliminar/<int:idRegistro>/', views.eliminar_registro, name='eliminar_registro'),
    path('informe/generar/', views.generar_informe, name='generar_informe'),
    path('informe/<int:idInforme>/', views.detalle_informe, name='detalle_informe'),
]
