from django.db import models

# Create your models here.
class  Servicios(models.Model):
    LUZ = 'luz'
    INTERNET = 'internet'
    AGUA = 'agua'
    GAS = 'gas'

    TIPO_SERVICIOS = (
                (LUZ, 'Luz'),
                (AGUA, 'Agua'),
                (GAS, 'Gas'),
                (INTERNET,'Internet')
                )

    nro_factura = models.CharField(max_length=100)
    fecha = models.DateField()
    servicio = models.CharField(max_length=10, choices=TIPO_SERVICIOS)
