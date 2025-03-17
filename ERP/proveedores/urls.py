from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_proveedores, name='lista_proveedores'),  # Listar todos los proveedores
    path('<int:idProveedor>/', views.detalle_proveedor, name='detalle_proveedor'),  # Detalle de un proveedor específico
    path('crear/', views.crear_proveedor, name='crear_proveedor'),  # Crear un nuevo proveedor
    path('modificar/<int:idProveedor>/', views.modificar_proveedor, name='modificar_proveedor'),
    path('eliminar/<int:idProveedor>/', views.eliminar_proveedor, name='eliminar_proveedor'),
]
