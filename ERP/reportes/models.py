# reportes/models.py
from django.db import models
from django.contrib.auth.models import User
from gestion_financiera.models import RegistroFinanciero
from inventario.models import Producto, MovimientoInventario
from pedidos.models import Pedido  # Correcto, referencia al modelo de pedidos
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime, timedelta

class Reporte(models.Model):
    idReporte = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50, choices=[('financiero', 'Financiero'), ('inventario', 'Inventario'), ('pedidos', 'Pedidos')])
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

  # reportes/models.py (solo el método _generar_reporte_pedidos)
    def _generar_reporte_pedidos(self):
        rango_inicio = self.parametros.get('rango_inicio')
        rango_fin = self.parametros.get('rango_fin')
        # Convertir las fechas a datetime para incluir todo el día
        inicio = datetime.strptime(rango_inicio, '%Y-%m-%d')
        fin = datetime.strptime(rango_fin, '%Y-%m-%d') + timedelta(days=1) - timedelta(seconds=1)  # Hasta el final del día
        pedidos = Pedido.objects.filter(fecha__gte=inicio, fecha__lte=fin)
        total_pedidos = pedidos.count()
        print(f"Rango ajustado: {inicio} - {fin}")
        print(f"Pedidos encontrados: {total_pedidos}")
        for p in pedidos:
            print(f"Pedido #{p.idPedido}: Fecha {p.fecha}, Cliente {p.cliente}, Total {p.total}")
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
    
    def __str__(self):
        return f"Reporte {self.tipo.capitalize()} generado el {self.fecha_generacion.strftime('%Y-%m-%d')}"