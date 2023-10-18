from django.db import models
#from personas.models import Cliente

class Estado(models.Model):
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.estado
    

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
class TipoDispositivo(models.Model):
    nombre = models.CharField(max_length=100) # Notebook, telefono, table..etc
    
    def __str__(self):
        return self.nombre
    
class Dispositivo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    num_serie = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoDispositivo, on_delete=models.CASCADE)
    imei = models.CharField(max_length=100, blank=True, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    #numero_orden = models.ForeignKey(Proveedor, on_delete=models.CASCADE) # numero de la orden de compra.
    observacion = models.TextField()
    
    
    def __str__(self):
        return f"{self.marca} {self.modelo} {self.num_serie} {self.tipo} {self.proveedor}"
    
class Software(models.Model):
    #moneda = (
    #    ('UF', 'unidad de fomento'),
    #    ('CL', 'Peso Chileno'),
    #    ('US', 'Dolar Americano'),
    #    ('AUD', 'Dolar Autraliano'),
    #    ('EU' , 'Euros'),
    #)
    
    tiempo_vida = (
        ('0', 'Permantente'),
        ('1', 'Un Año'),
        ('2', 'Dos años'),
        ('3','Tres años'),
    )
    
    nombre = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    cantidad_licencias = models.IntegerField(default=0)
    duracion = models.CharField(choices=tiempo_vida, default="1", max_length=5) # duracion en años
    fecha_registro = models.DateField(auto_now=True)
    fecha_compra = models.DateField(null=True, blank=True)
    fecha_caducidad = models.DateField(null=True, blank=True)
    #tipo_moneda = models.CharField(max_length=30, choices=moneda, blank=True, default='CL',
    #                               help_text="Tipo de moneda")
    #valor = models.FloatField()
    
    def __str__(self):
        return f"{self.nombre} {self.cantidad_licencias} {self.fecha_compra}"
    
    # realizar una funcion. para calcular el tiempo de vida del producto.
    
class Inventario(models.Model):
    tipo_hs = (
        ('H', 'Harware'),
        ('S', 'Software'),
    )
    nombre = models.CharField(max_length=100)
    #fecha_ingreso = models.DateField()
    valor = models.FloatField()
    numero_orden = models.CharField(max_length=80, blank=True, null=True)
    tipo = models.CharField(choices=tipo_hs, max_length=20) # tipo software o hardware
    disponible = models.BooleanField(default=False)
    #archivo = models.ImageField(upload_to="datos/", height_field=None, width_field=None, max_length=None, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True)
    software = models.ForeignKey(Software, on_delete=models.CASCADE, null=True)
    hadrware = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, null=True)
    
        

    
    
    
