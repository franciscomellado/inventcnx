from datetime import date, timedelta

from django.contrib.auth.models import User
from django.db import models
from inventario.models import Factura, Inventario, Software
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
    nombre = models.CharField(max_length=100)
    numero_identificacion = models.CharField(
        max_length=100, verbose_name="Número de identificación"
    )
    software = models.ForeignKey(
        Software, on_delete=models.CASCADE, related_name="licencias"
    )
    tipo_licencia = models.ForeignKey(TipoLicencia, on_delete=models.CASCADE)
    fecha_activacion = models.DateField()
    fecha_vencimiento = models.DateField(
        default=date.today() + timedelta(days=365), editable=False
    )
    completado = models.BooleanField(
        default=False,
        editable=False,
    )
    observacion = models.TextField()
    estado = models.ForeignKey(EstadoLic, on_delete=models.CASCADE)
    factura = models.ForeignKey(
        Factura, on_delete=models.CASCADE, related_name="facturas"
    )
    personasAsig = models.ManyToManyField(Persona, through="LicenciaUsuario")


class LicenciaUsuario(models.Model):
    person = models.ForeignKey(Persona, on_delete=models.CASCADE)
    licencias = models.ForeignKey(Licencia, on_delete=models.CASCADE)
    fecha_asignada = models.DateField()
    observacion = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now=True)
    usuario_asigna = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.usuario = User.objects.get(pk=self.usuario_id)
        super().save(*args, **kwargs)
