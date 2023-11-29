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
    usuario = models.CharField(max_length=100, null=True,blank=True)
    gerencia = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    @property
    def nombre_completo(self):
        nombre_completo = "%s %s" % (self.nombre, self.apellido)
        return nombre_completo.strip()

    def get_absolute_url(self):
        return reverse("personas:editar", kwargs={"id": self.id})
    
    