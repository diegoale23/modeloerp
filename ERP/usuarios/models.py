from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rol = models.CharField(
        max_length=20,
        choices=[
            ('administrador', 'Administrador'),
            ('empleado', 'Empleado'),
            ('cliente', 'Cliente')
        ]
    )
    email = models.EmailField(unique=True)

    # Solución a los conflictos: agregar related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios_set',  # Cambia el nombre del reverso para evitar conflictos
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_permissions_set',  # Cambia el nombre del reverso para evitar conflictos
        blank=True
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rol})"
