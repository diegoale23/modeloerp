from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_usuarios, name='lista_usuarios'),  # Listar todos los usuarios
    path('<int:idUsuario>/', views.detalle_usuario, name='detalle_usuario'),  # Detalle de un usuario específico
    path('crear/', views.crear_usuario, name='crear_usuario'),  # Crear un nuevo usuario
]
