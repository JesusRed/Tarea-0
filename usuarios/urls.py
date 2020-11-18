from django.urls import path
from . import views

urlpatterns = [
     # path del usuario
    path('registrar-usuario/',views.registrarUsuario,name="newUser"),
    path('misPqr/', views.misPqr, name="misPqr"),
] 