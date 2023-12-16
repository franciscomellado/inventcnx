from datetime import date, timedelta

from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from inventario.models import Software
from personas.models import Persona


class TipoLicencia(models.Model):
    tipo = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tipo

class EstadoLic(models.Model):
    estado = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.estado

class Licencia(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre de la licencia')
    numero_identificacion = models.CharField(max_length=100, verbose_name='Número de identificación',unique=True)
    software = models.ForeignKey(Software, on_delete=models.CASCADE, related_name="licencias")
    tipo_licencia = models.ForeignKey(TipoLicencia, on_delete=models.CASCADE, verbose_name='Tipo de licencia')
    fecha_activacion = models.DateField(auto_now_add=True, verbose_name='Fecha de activación')
    fecha_vencimiento = models.DateField(default=date.today() + timedelta(days=365), editable=False,verbose_name='Fecha de vencimiento')  
    observaciones = models.TextField(verbose_name='Observaciones', null=True,blank=True)
    estado = models.ForeignKey(EstadoLic, on_delete=models.PROTECT, verbose_name='Estado de la licencia')
    asignada = models.BooleanField(default=False )
   
    def __str__(self):
        return f'{self.nombre} - {self.numero_identificacion} -software: {self.software.marca}  {self.software.version}'
    
    # def get_absolute_url(self):
    #     return reverse("licencias: index", kwargs={"id": self.id})
    
class LicenciaUsuario(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE,related_name='personas_asignadas')
    licencia = models.OneToOneField(Licencia, on_delete=models.CASCADE,  null=True, blank=True, related_name='licencia_asignada')
    fecha_asignada = models.DateField(verbose_name='Fecha de asignación')
    observacion = models.TextField(max_length=100, verbose_name='Observaciones',null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now=True, verbose_name='Fecha de registro')
    creado_por=models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['persona', 'licencia'], 
                name='LicenciaUnica'
            )
        ]
    
    def __str__(self):
        return f'{self.persona.nombre} {self.persona.apellido} '
    
    def clean(self):
        if not self.licencia:
            raise ValidationError('Debe seleccionar una licencia.')
        # Verificar si la persona ya tiene una licencia para el software específico
        if LicenciaUsuario.objects.filter(persona=self.persona, licencia__software=self.licencia.software).exists():
            raise ValidationError('Esta persona ya tiene una licencia para este software.')
    
@receiver(post_save, sender=LicenciaUsuario)
def update_licencia_asignada(sender, instance, **kwargs):
    licencia_usuario = instance
    licencia = licencia_usuario.licencia
    licencia.asignada = True
    licencia.save()

    