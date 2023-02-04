from django.urls import path
#Vamos a importar todas las funciones creadas en el Views
#le ponermos  un . poruqe urls y views estan en el mismo nivel

from . import views
urlpatterns = {
    path("hola", views.holaEndpoint),
    path("adios", views.adiosEndpoint)
}