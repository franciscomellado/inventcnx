from django.db import models
from personas.models import Cliente

class Estado(models.Model):
    estado = models.CharField(max_length=100)
    desripcion = models.TextField()
    

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    
    def __str__(self):
        #return self.nombre, self.codigo, self.contacto
        return f"{self.nombre} {self.codigo} {self.contacto}"
    
    
class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
    
class Dispositivo(models.Model):
    dispositivo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    observacion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    imei = models.CharField(max_length=100)
    num_serie = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    
    
class Software(models.Model):
    moneda = (
        ('UF', 'unidad de fomento'),
        ('CL', 'Peso Chileno'),
        ('US', 'Dolar Americano'),
        ('AUD', 'Dolar Autraliano'),
        ('EU' , 'Euros'),
    )
    nombre = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    cantidad_licencias = models.IntegerField(default=0)
    duracion = models.IntegerField(default=0)
    fecha_compra = models.DateTimeField("Fecha de ingreso")
    fecha_caducidad = models.DateTimeField("Feha de caducidad")
    valor = models.FloatField()
    tipo_moneda = models.CharField(max_length=30, choices=moneda, blank=True, default='CL',
                                   help_text="Tipo de moneda")
    
    def __str__(self):
        return f"{self.nombre} {self.cantidad_licencias} {self.fecha_compra}"
    
class Inventario(models.Model):
    nombre = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField("Fecha de ingreso")
    valor = models.FloatField()
    numero_orden = models.CharField(max_length=80)
    tipo = models.CharField(max_length=100)
    disponible = models.BooleanField(default=False)
    archivo = models.ImageField(upload_to="datos/", height_field=None, width_field=None, max_length=None)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    software = models.ForeignKey(Software, on_delete=models.CASCADE)
        

    
    
    
