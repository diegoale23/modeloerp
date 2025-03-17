from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Ruta para la administración de Django
    path('admin/', admin.site.urls),

    # Rutas para las aplicaciones del ERP
    path('usuarios/', include('usuarios.urls')),  # URLs de la app usuarios
    path('pedidos/', include('pedidos.urls')),  # URLs de la app pedidos
    path('proveedores/', include('proveedores.urls')),  # URLs de la app proveedores
    path('gestion-financiera/', include('gestion_financiera.urls')),  # URLs de la app gestion_financiera
    path('inventario/', include('inventario.urls')),  # URLs de la app inventario
    path('reportes/', include('reportes.urls')),  # URLs de la app reportes
    path('productos/', include('productos.urls')),# URLs de la app productos

    # Rutas para login/logout
    #path('auth/', include('django.contrib.auth.urls')),  # URLs predefinidas para autenticación
]