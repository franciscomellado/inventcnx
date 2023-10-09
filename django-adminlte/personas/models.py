from django.db import models

class Area(models.Model):
    nombre = models.CharField(max_length=100)

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    
class Prestamo(models.Model):
    nombre =models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField()
    fecha_devolucion = models.DateTimeField()
    
    
    
    