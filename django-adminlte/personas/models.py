from django.db import models
from django.urls import reverse
class Area(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre}"
    def get_absolute_url(self):
         return reverse("personas:index")
    

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre}"
    def get_absolute_url(self):
         return reverse("personas:index")
    

class Personas(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Personas"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    def get_absolute_url(self):
        print(self)
        return reverse("personas:index")
    
class Prestamo(models.Model):
    nombre =models.ForeignKey(Personas, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField()
    fecha_devolucion = models.DateTimeField()
    
    
    
    