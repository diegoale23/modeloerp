from django.db import models

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        self.save()

    def consultar_disponibilidad(self):
        return self.stock > 0
