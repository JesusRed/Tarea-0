from django.urls import path
from pqrs import views

urlpatterns = [

    # path de las pqr
    path('registrar-pqr/' ,views.registrarPqr,name="newPqr"),
    path('insertar-pqr/' , views.insertarPqr),
    # path('',views.MostrarPqr,name="mostrarPqrs"),
    # path('',views.MostrarPqrs,name="mostrarPqrs"),
] 