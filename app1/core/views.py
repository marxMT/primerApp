from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from core.models import Servicios
from core.serializers import ServiciosSerializar

# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONResponse().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content,**kwargs)


@csrf_exempt
def servicios_lista(request):
    if request.method == 'GET':
        servicios = Servicios.object.all()
        serializer = ServiciosSerializar(servicios, many=True)
        return JSONResponse(serializer.data)
    elif request.method =='POST':
        data =JSONParser().parse(request)
        serializer = ServiciosSerializar(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def servicio_detail(request, pk):
    try:
        servicios = Servicios.object.all(pk=pk)
    except servicios.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ServiciosSerializar(serie)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().render(request)
        serializer = ServiciosSerializar(serie, data=data)
        if serializer.is_valid():
            serializer.saver()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.error, status=404)
    elif request.method == 'DELETE':
        servicios.delete()
        return HttpResponse(status=204)
        
