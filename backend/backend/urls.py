#Vamos a importar todas las funciones creadas en el Views y en urls de prueba
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("prueba/", include("prueba.urls")),
    path('admin/', admin.site.urls),
]
