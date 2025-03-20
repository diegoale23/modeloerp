# reportes/models.py
from django.db import models
from django.contrib.auth.models import User
from gestion_financiera.models import RegistroFinanciero
from inventario.models import Producto, MovimientoInventario
from pedidos.models import Pedido
from proveedores.models import Proveedor  # Importamos Proveedor
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime, timedelta

class Reporte(models.Model):
    idReporte = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50, choices=[
        ('financiero', 'Financiero'),
        ('inventario', 'Inventario'),
        ('pedidos', 'Pedidos'),
        ('proveedores', 'Proveedores')  # Nuevo tipo de reporte
    ])
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    parametros = models.JSONField(encoder=DjangoJSONEncoder)
    contenido = models.TextField()
    generado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def generar(self, tipo, usuario, **parametros):
        self.tipo = tipo
        self.parametros = parametros
        self.generado_por = usuario
        if tipo == 'financiero':
            self._generar_reporte_financiero()
        elif tipo == 'inventario':
            self._generar_reporte_inventario()
        elif tipo == 'pedidos':
            self._generar_reporte_pedidos()
        elif tipo == 'proveedores':
            self._generar_reporte_proveedores()  # Nuevo método
        else:
            raise ValueError("Tipo de reporte no soportado.")
        self.save()

    def _generar_reporte_financiero(self):
        rango_inicio = self.parametros.get('rango_inicio')
        rango_fin = self.parametros.get('rango_fin')
        registros = RegistroFinanciero.objects.filter(fecha__range=(rango_inicio, rango_fin))
        ingresos = registros.filter(tipo='ingreso').aggregate(models.Sum('monto'))['monto__sum'] or 0
        gastos = registros.filter(tipo='gasto').aggregate(models.Sum('monto'))['monto__sum'] or 0
        balance = ingresos - gastos
        detalle_ingresos = "\n".join([f"{r.fecha}: ${r.monto} - {r.descripcion or 'Sin descripción'}" for r in registros.filter(tipo="ingreso")])
        detalle_gastos = "\n".join([f"{r.fecha}: ${r.monto} - {r.descripcion or 'Sin descripción'}" for r in registros.filter(tipo="gasto")])
        self.contenido = (
            f"Reporte Financiero\n"
            f"=================\n"
            f"Período: {rango_inicio} a {rango_fin}\n"
            f"Ingresos Totales: ${ingresos}\n"
            f"Gastos Totales: ${gastos}\n"
            f"Balance: ${balance}\n\n"
            f"Detalle de Ingresos\n"
            f"------------------\n"
            f"{detalle_ingresos or 'No hay ingresos'}\n\n"
            f"Detalle de Gastos\n"
            f"-----------------\n"
            f"{detalle_gastos or 'No hay gastos'}"
        )

    def _generar_reporte_inventario(self):
        rango_inicio = self.parametros.get('rango_inicio')
        rango_fin = self.parametros.get('rango_fin')
        productos = Producto.objects.all()
        estado_productos = "\n".join([f"{p.nombre}: Stock {p.stock}, Precio ${p.precio}" for p in productos])
        movimientos = MovimientoInventario.objects.filter(fecha__range=(rango_inicio, rango_fin))
        detalle_movimientos = "\n".join([f"{m.fecha.strftime('%Y-%m-%d %H:%M')}: {m.tipo.capitalize()} de {m.cantidad} - {m.producto.nombre} ({m.descripcion or 'Sin descripción'})" for m in movimientos])
        self.contenido = (
            f"Reporte de Inventario\n"
            f"====================\n"
            f"Período: {rango_inicio} a {rango_fin}\n\n"
            f"Estado Actual de Productos\n"
            f"-------------------------\n"
            f"{estado_productos or 'No hay productos'}\n\n"
            f"Movimientos de Inventario\n"
            f"------------------------\n"
            f"{detalle_movimientos or 'No hay movimientos en este período'}"
        )

    def _generar_reporte_pedidos(self):
        rango_inicio = self.parametros.get('rango_inicio')
        rango_fin = self.parametros.get('rango_fin')
        inicio = datetime.strptime(rango_inicio, '%Y-%m-%d')
        fin = datetime.strptime(rango_fin, '%Y-%m-%d') + timedelta(days=1) - timedelta(seconds=1)
        pedidos = Pedido.objects.filter(fecha__gte=inicio, fecha__lte=fin)
        total_pedidos = pedidos.count()
        contenido = "\n".join([f"Pedido #{p.idPedido}: Cliente {p.cliente.nombre} {p.cliente.apellido}, Total ${p.total}" for p in pedidos])
        self.contenido = (
            f"Reporte de Pedidos\n"
            f"=================\n"
            f"Período: {rango_inicio} a {rango_fin}\n"
            f"Total de Pedidos: {total_pedidos}\n\n"
            f"Pedidos\n"
            f"-------\n"
            f"{contenido or 'No hay pedidos'}"
        )

    def _generar_reporte_proveedores(self):
        # No usamos rango de fechas porque no hay un campo temporal en Proveedor
        proveedores = Proveedor.objects.all()
        total_proveedores = proveedores.count()
        detalle_proveedores = "\n".join([
            f"{p.nombre}: Contacto {p.contacto}, Email {p.email}, Productos: {', '.join([prod.nombre for prod in p.productos.all()])}"
            if p.productos.exists() else f"{p.nombre}: Contacto {p.contacto}, Email {p.email}, Productos: Ninguno"
            for p in proveedores
        ])
        self.contenido = (
            f"Reporte de Proveedores\n"
            f"=====================\n"
            f"Total de Proveedores: {total_proveedores}\n\n"
            f"Detalle de Proveedores\n"
            f"---------------------\n"
            f"{detalle_proveedores or 'No hay proveedores'}"
        )

    def __str__(self):
        return f"Reporte {self.tipo.capitalize()} generado el {self.fecha_generacion.strftime('%Y-%m-%d')}"