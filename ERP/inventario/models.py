from django.db import models

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)  # Identificador único
    nombre = models.CharField(max_length=100)  # Nombre del producto
    descripcion = models.TextField(blank=True, null=True)  # Descripción del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto
    stock = models.IntegerField(default=0)  # Cantidad en inventario
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de registro del producto

    def actualizar_stock(self, cantidad):
        # Método para actualizar el stock del producto
        self.stock += cantidad
        self.save()

    def consultar_disponibilidad(self):
        # Método para verificar si el producto está disponible
        return self.stock > 0

    def __str__(self):
        return f"{self.nombre} ({self.stock} disponibles)"

class MovimientoInventario(models.Model):
    TIPO_CHOICES = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    ]
    idMovimiento = models.AutoField(primary_key=True)  # Identificador único del movimiento
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Producto relacionado
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)  # Tipo de movimiento
    cantidad = models.IntegerField()  # Cantidad del movimiento
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha del movimiento
    descripcion = models.TextField(blank=True, null=True)  # Detalles opcionales del movimiento

    def aplicar_movimiento(self):
        # Método para ajustar el stock del producto en función del movimiento
        if self.tipo == 'entrada':
            self.producto.actualizar_stock(self.cantidad)
        elif self.tipo == 'salida' and self.cantidad <= self.producto.stock:
            self.producto.actualizar_stock(-self.cantidad)
        else:
            raise ValueError("La cantidad de salida excede el stock disponible")
        self.save()

    def __str__(self):
        return f"{self.tipo.capitalize()} de {self.cantidad} - {self.producto.nombre}"
