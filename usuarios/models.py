from django.db import models

# Create your models here.
class Usuario(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=100)
    email= models.CharField(verbose_name="Correo", max_length=100)
    password = models.CharField(verbose_name="Password", max_length=100)

    class Meta:
        verbose_name= "Usuario"
        verbose_name_plural= "Usuarios"
    
    def __str__(self):
        return self.name
