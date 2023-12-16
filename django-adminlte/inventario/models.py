import os
from pyexpat import model
from django.db import models
from personas.models import Persona
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from datetime import date, timedelta, datetime
from .utils.resize import resize_image
class Estado(models.Model):
    estado = models.CharField(max_length=100,  unique=True)

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
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre
class TipoDispositivo(models.Model):
    nombre = models.CharField(max_length=100, unique=True) # Notebook, telefono, table..etc
    
    def __str__(self):
        return self.nombre

class Factura(models.Model):
    factura = models.CharField(max_length=100)
    fecha_factura = models.DateField()
    facturapdf = models.FileField(upload_to="facturas/", null=True, blank=True)
    fecha_registro = models.DateField(auto_now=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, null=True)
    orden_de_compra = models.CharField(max_length=50,null=True,blank=True)
    observacion = models.TextField(null=True, blank=True, verbose_name="observaciones")
    
    def __str__(self):
        return self.factura
    
class CustomManager(models.Manager):
    def delete(self):
        for obj in self.get_queryset():
            obj.delete()
class Dispositivo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    num_serie = models.CharField(max_length=100, unique=True)
    tipo_dispositivo = models.ForeignKey(TipoDispositivo, on_delete=models.CASCADE)
    imei = models.CharField(max_length=100, blank=True, null=True)
    imagen_dispositivo = models.ImageField(upload_to="datos/dispositivos/", null=True, blank=True, verbose_name="Foto Dispositivo")
    persona_asignada = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, blank=True)
    inventario = GenericRelation(
        "Inventario", "object_id", "content_type", related_query_name="dispositivo",
    )
    objects = CustomManager() # just add this line of code inside of your model

    def delete(self,*args,**kwargs):
        
        if self.imagen_dispositivo and os.path.isfile(self.imagen_dispositivo.path):
            os.remove(self.imagen_dispositivo.path)
        super(Dispositivo, self).delete(*args,**kwargs)
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.imagen_dispositivo:
            resize_image(self.imagen_dispositivo.path)
            
    def __str__(self):
        return f"{self.marca} {self.modelo} {self.num_serie}"


class Software(models.Model):
    marca = models.ForeignKey(Marca,max_length=100, on_delete=models.CASCADE)
    version = models.CharField(max_length=100)
    fecha_instalacion = models.DateField(verbose_name="Fecha de instalación", null=True,blank=True)
    cuenta_asociada = models.CharField(max_length=100, null=True,blank=True)
    cantidad_licencias = models.IntegerField(default=1)
    cantidad_disponibles = models.IntegerField(editable=False, default=0)
    inventario = GenericRelation(
        "Inventario", "object_id", "content_type", related_query_name="software", 
    )
    
    def __str__(self):
        return f"{self.marca} {self.version}"
    
class Inventario(models.Model):

    DURACION = (
        ('0', 'Permanente'),
        ('1', 'Un Año'),
        ('2', 'Dos años'),
        ('3','Tres años'),
        ('4','Cuatro años'),
    )
    LIMIT = models.Q(app_label='inventario', model='dispositivo') | models.Q (app_label='inventario', model='software')
    
    nombre = models.CharField(max_length=100)
    valor = models.FloatField()
    disponible = models.BooleanField(default=False)
    duracion = models.CharField(choices=DURACION, default="0", max_length=5) # duracion en años
    fecha_registro = models.DateField(auto_now=True)
    fecha_entrega = models.DateField(null=True, blank=True)
    fecha_modificacion = models.DateField(default=date.today)
    fecha_caducidad = models.DateField(null=True, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, null=True,blank=True)
    observacion = models.TextField(null=True, blank=True,verbose_name="observaciones")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to=LIMIT )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def calcular_fecha_caducidad(self):
        if self.fecha_entrega and (self.duracion != '0'):
            years = int(self.duracion)
            days = years * 365 + years // 4  
            return  self.fecha_entrega + timedelta(days=days)
        return None
    
    @property
    def tiempo_de_vida(self):
        if self.fecha_entrega and self.duracion:
            fecha_actual = datetime.now().date()
            tiempo_de_vida = self.fecha_caducidad - fecha_actual
        return tiempo_de_vida.days
    
    def save(self, *args, **kwargs):       
        if self.pk:  # Si el objeto ya existe en la base de datos
            old_obj = Inventario.objects.get(pk=self.pk)  # Obtener el objeto anterior
            if old_obj.duracion != self.duracion:  # Si la duración ha cambiado
                self.fecha_caducidad = self.calcular_fecha_caducidad()  # Calcular la nueva fecha de caducidad
        else:  # Si el objeto es nuevo
            self.fecha_caducidad = self.calcular_fecha_caducidad()  # Calcular la fecha de caducidad inicial
        super().save(*args, **kwargs)  # Llamar al método save de la superclase para guardar el objeto
    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
    def __str__(self):
        return f"{self.nombre} {self.valor} {self.estado}"
    
    def get_absolute_url(self):
        return reverse("inventario: index", kwargs={"id": self.id})



    
    
    
