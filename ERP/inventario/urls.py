from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),  # Listar todos los productos
    path('<int:idProducto>/', views.detalle_producto, name='detalle_producto'),  # Detalle de un producto específico
    path('registrar-movimiento/', views.registrar_movimiento, name='registrar_movimiento'),  # Registrar un movimiento de inventario
]
