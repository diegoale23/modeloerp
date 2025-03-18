from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pedidos, name='lista_pedidos'),  # Listar todos los pedidos
    path('<int:idPedido>/', views.detalle_pedido, name='detalle_pedido'),  # Detalle de un pedido específico
    path('crear/', views.crear_pedido, name='crear_pedido'),  # Crear un nuevo pedido
    path('modificar/<int:idPedido>/', views.modificar_pedido, name='modificar_pedido'),
    path('eliminar/<int:idPedido>/', views.eliminar_pedido, name='eliminar_pedido'),
]
