from rest_framework import serializers
from .models import Servicios

class ServiciosSerializar(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    servicio = serializers.CharField()
    fecha = serializers.DateField()
    nro_factura = serializers.CharField()

    def create(self, validated_data):
        instance = Servicios()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        instance.nro_factura = validated_data.get('nro_factura')
        instance.servicio = validated_data.get('servicio')
        instance.fecha = validated_data.get('fecha')
        instance.save()
        return instance
