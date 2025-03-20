# proveedores/models.py
from django.db import models
from inventario.models import Producto  # Importamos el modelo Producto

class Proveedor(models.Model):
    idProveedor = models.AutoField(primary_key=True)  # Identificador único
    nombre = models.CharField(max_length=100)  # Nombre del proveedor
    contacto = models.CharField(max_length=100)  # Nombre de la persona de contacto
    direccion = models.TextField()  # Dirección del proveedor
    telefono = models.CharField(max_length=15)  # Número de teléfono
    email = models.EmailField(unique=True)  # Correo electrónico
    productos = models.ManyToManyField(Producto, blank=True, related_name='proveedores')  # Relación muchos a muchos con Producto

    def registrar_proveedor(self):
        # Método para registrar un proveedor en la base de datos
        self.save()

    def gestionar_ordenes(self):
        # Método para manejar órdenes relacionadas (puedes desarrollarlo más)
        pass

    def __str__(self):
        return self.nombre