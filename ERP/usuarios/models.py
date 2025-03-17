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
        ],
        default='cliente'  # Agregar valor por defecto
    )
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_permissions_set',
        blank=True
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rol})"