from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_proveedores, name='lista_proveedores'),  # Listar todos los proveedores
    path('<int:idProveedor>/', views.detalle_proveedor, name='detalle_proveedor'),  # Detalle de un proveedor específico
    path('crear/', views.crear_proveedor, name='crear_proveedor'),  # Crear un nuevo proveedor
]
