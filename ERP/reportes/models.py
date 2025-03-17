from django.db import models

class Reporte(models.Model):
    idReporte = models.AutoField(primary_key=True)  # Identificador único
    tipo = models.CharField(max_length=50, choices=[('financiero', 'Financiero'), ('inventario', 'Inventario'), ('pedidos', 'Pedidos')])  # Tipo de reporte
    fecha_generacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    parametros = models.JSONField()  # Parámetros usados para generar el reporte (e.g., rango de fechas)
    contenido = models.TextField()  # Contenido del reporte (puede incluir un resumen o datos procesados)
    generado_por = models.ForeignKey('usuarios.Usuario', on_delete=models.SET_NULL, null=True)  # Referencia al usuario que generó el reporte

    def generar(self, parametros):
        # Método para generar el contenido del reporte basado en los parámetros
        self.parametros = parametros
        self.save()

    def descargar(self):
        # Método para descargar el reporte en formatos específicos (e.g., PDF, CSV)
        pass

    def __str__(self):
        return f"Reporte {self.tipo} generado el {self.fecha_generacion.strftime('%Y-%m-%d')}"
