from django.urls import path
#Vamos a importar todas las funciones creadas en el Views
#le ponermos  un . poruqe urls y views estan en el mismo nivel

from . import views
urlpatterns = {
    path("hola", views.holaEndpoint),
    path("adios", views.adiosEndpoint),
    path("html", views.htmlEndpoint),
    path("post", views.postFormularioEndpoint),
    #Hacer peticiones http, mediante links
    path("get-query",views.getQueryParameters),
    path("get-path/<str:username>/<str:password>",views.getPathParameters),
    path("post-raw", views.getRawData)
    
}