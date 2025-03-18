# gestion_financiera/models.py
from django.db import models
from usuarios.models import Usuario  # Modelo de clientes
from django.contrib.auth.models import User  # Modelo por defecto para autenticación

class RegistroFinanciero(models.Model):
    idRegistro = models.AutoField(primary_key=True)
    TIPO_CHOICES = [
        ('ingreso', 'Ingreso'),
        ('gasto', 'Gasto'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)  # Cliente al que se asocia el movimiento

    def __str__(self):
        return f"{self.tipo.capitalize()} de {self.monto} el {self.fecha}"

class InformeFinanciero(models.Model):
    idInforme = models.AutoField(primary_key=True)
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    rango_inicio = models.DateField()
    rango_fin = models.DateField()
    contenido = models.TextField()
    generado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Usuario autenticado que genera el informe

    def generar_informe(self):
        registros = RegistroFinanciero.objects.filter(fecha__range=(self.rango_inicio, self.rango_fin))
        ingresos = registros.filter(tipo="ingreso").aggregate(models.Sum('monto'))['monto__sum'] or 0
        gastos = registros.filter(tipo="gasto").aggregate(models.Sum('monto'))['monto__sum'] or 0
        balance = ingresos - gastos

        detalle_ingresos = "\n".join([f"{r.fecha}: ${r.monto} - {r.descripcion or 'Sin descripción'}" for r in registros.filter(tipo="ingreso")])
        detalle_gastos = "\n".join([f"{r.fecha}: ${r.monto} - {r.descripcion or 'Sin descripción'}" for r in registros.filter(tipo="gasto")])

        self.contenido = (
            f"Resumen Financiero\n"
            f"==================\n"
            f"Período: {self.rango_inicio} a {self.rango_fin}\n"
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
        self.save()

    def __str__(self):
        return f"Informe del {self.rango_inicio} al {self.rango_fin} generado el {self.fecha_generacion}"