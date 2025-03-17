from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('<int:idProducto>/', views.detalle_producto, name='detalle_producto'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('registrar-movimiento/', views.registrar_movimiento, name='registrar_movimiento'),
    path('<int:idProducto>/editar/', views.editar_producto, name='editar_producto'),
    path('<int:idProducto>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
]