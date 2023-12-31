from django.db import models
from personas.models import Persona

class Estado(models.Model):
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.estado
    

class Proveedor(models.Model): # Distribuidor 
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

class Factura(models.Model):
    factura = models.CharField(max_length=100)
    
    def __str__(self):
        return self.factura
class Dispositivo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    num_serie = models.CharField(max_length=100, unique=True)
    tipo = models.ForeignKey(TipoDispositivo, on_delete=models.CASCADE)
    imei = models.CharField(max_length=100, blank=True, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    fecha_registro = models.DateField(auto_now=True)
    fecha_compra = models.DateField(null=True, blank=True)
    fecha_caducidad = models.DateField(null=True, blank=True)
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
        ('4','Cuatro años'),
    )
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca,max_length=100, on_delete=models.CASCADE)
    version = models.CharField(max_length=100)
    cantidad_licencias = models.IntegerField(default=0)
    duracion = models.CharField(choices=tiempo_vida, default="0", max_length=5) # duracion en años
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    fecha_registro = models.DateField(auto_now=True)
    fecha_compra = models.DateField(null=True, blank=True)
    fecha_caducidad = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} {self.cantidad_licencias} {self.fecha_compra}"
    
    # realizar una funcion. para calcular el tiempo de vida del producto.
    
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
class Inventario(models.Model):
    tipo_hs = (
        ('H', 'Hardware'),
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
    #software = models.ForeignKey(Software, on_delete=models.CASCADE, null=True)
    #hadrware = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, null=True)
    persona_asignada = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, blank=True)
        
# como vamos hacer la asignación de equipos y software para las personas. Vmaos a usar esta misma tabla
# o realizamos una nueva aplicacion.
 # Para la asignación de equipos y software a las personas, En la misma tabla Inventario y agregar un nuevo campo que indique a qué persona está asignado el producto. De esta manera, podrías relacionar los productos de inventario con las personas correspondientes.

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=1 )
    object_id = models.PositiveIntegerField(default=1)
    contenido = GenericForeignKey('content_type', 'object_id')



    
    
    
