from django.shortcuts import render
from django.http import HttpResponse
# Dentro de los Views hay código que se va ejecutar ante la llegada de una petición  http.
#Para ejecutar estas funciones a partir de las urls debemos configurar las rutas
#primero en urls de prueba y urls en backend
def holaEndpoint(request):
    #request es un objeto

    return HttpResponse("HOLA!!!")#Necesitamos importar para usar HttpResponse
def adiosEndpoint(request):
    return HttpResponse("ADIOS!!!")