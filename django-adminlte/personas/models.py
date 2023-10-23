from django.db import models
from django.urls import reverse

class Departamento(models.Model): # nombre de  la genencia.
    gerencia = models.CharField(max_length=100)

    def __str__(self):
        return self.gerencia    

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    gerencia = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    def get_absolute_url(self):
        return reverse("editar", kwargs={"id": self.id})
    
    