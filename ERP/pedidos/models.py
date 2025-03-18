from django.db import models
from usuarios.models import Usuario
from inventario.models import Producto  # Importamos desde inventario

class Pedido(models.Model):
    idPedido = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('procesado', 'Procesado')], default='pendiente')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedidos')  # Añadimos related_name
    productos = models.ManyToManyField(Producto, through='DetallePedido')

    def __str__(self):
        return f"Pedido #{self.idPedido} - {self.cliente}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre} (x{self.cantidad})"