from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('informacion/', views.informacion, name="infomacion"),
]