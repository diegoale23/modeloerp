from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import index  # Importamos la vista index

urlpatterns = [
    # Ruta para la administración de Django
    path('admin/', admin.site.urls),

    # Ruta raíz muestra el login
    path('', auth_views.LoginView.as_view(
        template_name='login.html',
        redirect_authenticated_user=True,
        next_page='/index/'  # Redirige a /index/ tras login
    ), name='home'),

    # Ruta para la página index
    path('index/', index, name='index'),

    # Rutas para las aplicaciones del ERP
    path('usuarios/', include('usuarios.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('proveedores/', include('proveedores.urls')),
    path('gestion-financiera/', include('gestion_financiera.urls')),
    path('inventario/', include('inventario.urls')),
    path('reportes/', include('reportes.urls')),
    #path('productos/', include('productos.urls')),

    # Ruta para login
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html',
        redirect_authenticated_user=True,
        next_page='/index/'  # Redirige a /index/ tras login
    ), name='login'),

    # Ruta para logout
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
]