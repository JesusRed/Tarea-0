from django.shortcuts import render
from .models import Pqrs
# from django.contrib.auth.models import User
import datetime

def registrarPqr(request):
 
    return render(request,"pqrs/newpqr.html")
    
def insertarPqr(request):
    # print('ACAAAAAAAAAAAAAAA')
    asunto=request.GET["asunto"]
    tipo=request.GET["tipo"]
    cuerpo=request.GET["cuerpo"]
    print(asunto,tipo)
    pqr=Pqrs(create_at=datetime.datetime.now(),subject=asunto,descripcion=cuerpo,tipo=tipo,state='2')
    pqr.save()
    print(asunto,tipo)
    pqrs=Pqrs.objects.all()
    print(pqrs)
    return render(request,"usuarios/mispqr.html")



