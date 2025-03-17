from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),  # Listar todos los productos
    path('<int:idProducto>/', views.detalle_producto, name='detalle_producto'),  # Detalle de un producto específico
    path('crear/', views.crear_producto, name='crear_producto'),  # Crear un nuevo producto
    path('<int:idProducto>/editar/', views.editar_producto, name='editar_producto'),  # Editar un producto existente
    path('<int:idProducto>/eliminar/', views.eliminar_producto, name='eliminar_producto'),  # Eliminar un producto
]
