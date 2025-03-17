from django.db import models
from usuarios.models import Usuario  # Relación con la tabla de usuarios

class RegistroFinanciero(models.Model):
    idRegistro = models.AutoField(primary_key=True)  # Identificador único
    TIPO_CHOICES = [
        ('ingreso', 'Ingreso'),
        ('gasto', 'Gasto'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)  # Tipo de registro (Ingreso o Gasto)
    monto = models.DecimalField(max_digits=12, decimal_places=2)  # Monto del registro
    descripcion = models.TextField(blank=True, null=True)  # Descripción opcional
    fecha = models.DateField(auto_now_add=True)  # Fecha del registro
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)  # Usuario que registró el movimiento

    def __str__(self):
        return f"{self.tipo.capitalize()} de {self.monto} el {self.fecha}"

class InformeFinanciero(models.Model):
    idInforme = models.AutoField(primary_key=True)  # Identificador único
    fecha_generacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación del informe
    rango_inicio = models.DateField()  # Fecha inicial del rango del informe
    rango_fin = models.DateField()  # Fecha final del rango del informe
    contenido = models.TextField()  # Contenido generado del informe (puede incluir un resumen)
    generado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)  # Usuario que generó el informe

    def generar_informe(self):
        # Método para procesar y generar el contenido del informe
        registros = RegistroFinanciero.objects.filter(fecha__range=(self.rango_inicio, self.rango_fin))
        ingresos = registros.filter(tipo="ingreso").aggregate(models.Sum('monto'))['monto__sum'] or 0
        gastos = registros.filter(tipo="gasto").aggregate(models.Sum('monto'))['monto__sum'] or 0
        balance = ingresos - gastos
        self.contenido = f"Ingresos: {ingresos}, Gastos: {gastos}, Balance: {balance}"
        self.save()

    def __str__(self):
        return f"Informe del {self.rango_inicio} al {self.rango_fin} generado el {self.fecha_generacion}"

