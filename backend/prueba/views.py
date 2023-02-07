from django.shortcuts import render
from django.http import HttpResponse
#Para desavilitar una medida de seguridad y retornar "postFormularioEndpoint" cuando demos click al botom.
from django.views.decorators.csrf import csrf_exempt
import json #PAra conertir a String json

# Dentro de los Views hay código que se va ejecutar ante la llegada de una petición  http.
#Para ejecutar estas funciones a partir de las urls debemos configurar las rutas
#primero en urls de prueba y urls en backend
def holaEndpoint(request):
    #request es un objeto
    return HttpResponse("HOLA!!!")#Necesitamos importar para usar HttpResponse
def adiosEndpoint(request):
    return HttpResponse("ADIOS!!!")

def htmlEndpoint(request):
    return HttpResponse(
        """
        <html>
              <body>
                    <h1>Programacion Web</h1>
                    <br/>
                    <br/>
                    <img src="https://cdn.pixabay.com/photo/2017/02/09/21/08/wings-2053515__340.png"/>
                    <!-- 
Lo que yo agregué a la caja de texto(a los input) se va a enviar como una petición http al servidor
Para poder definir en dónde vamos enviar la información, a donde realizamos la petición http
post = al mismo servidor.
El nombre(name) sirve para identificar el valor de ese campo.
                    -->
                    <form method="post" action="/prueba/post">
                          <br/>
                          <input type="text" name="username"/>
                          <br/>
                          <input type="password" name="password"/>
                          <br/>
                          <button type="submit">Enviar</button>
                    </form>
              </body>
        </html>
        """
    )
#Ruta: /post
@csrf_exempt
def postFormularioEndpoint(request):
    if request.method == "POST":#Si es un metodo POST
        username = request.POST.get("username")
        password = request.POST.get("password")
        return HttpResponse(f"""
        <p>Usuario: {username}</p> <!-- interpolacion de String, importante poner la f cuando lo hacemos-->
        <p>Password: {password}</p>
        """)
    return HttpResponse("Llego")
def getQueryParameters(request):
    if request.method == "GET":
        username = request.GET.get("usu")
        password = request.GET.get("pass")
        return HttpResponse(f"""
        <p>Usuario: {username}</p> 
        <p>Password: {password}</p>
        """
        )
def getPathParameters(request, username, password):
    if request.method == "GET":
        return HttpResponse(f"""
        <p>Usuario: {username}</p> 
        <p>Password: {password}</p>
        """
        )
@csrf_exempt
def getRawData(request):
    if request.method == "POST":
        strBody = request.body
        dictUsuario = json.loads(strBody) #Convierte String(json) --> objeto diccionario python
        jsonUsuario = json.dumps(dictUsuario) #De dicc a String
        #f"""
        #<p>Usuario: {dictUsuario["username"]}</p>
        #<p>Clave: {dictUsuario["password"]}</p>
        #"""
        return HttpResponse(jsonUsuario)


