from django.db import models
# from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Pqrs(models.Model):

    tipos=(('1','PETICION'),('2','QUEJA'),('3','RECLAMO'))
    states=(('1','EN PROGRESO'),('2','EN ESPERA'),('3','RESPONDIDA'))
    state=models.CharField(max_length=20,choices=states,default='2')
    tipo=models.CharField(max_length=20,choices=tipos,default='1')
    subject=models.CharField(max_length=50)
    descripcion=models.TextField()
    create_at=models.TimeField(default=datetime.now())
    nota=models.TextField(null=True,blank=True)
    response_at=models.TimeField(null=True, blank=True)
   # author=models.ForeignKey(User,verbose_name='usuario',on_delete=models.CASCADE)
