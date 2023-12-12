from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from inventario.models import Proveedor, Dispositivo,Software,Factura,Inventario
from licencias.models import Licencia,LicenciaUsuario
from personas.models import Persona


# Create your views here.
@login_required
def index(request):
    cantpersonas = Persona.objects.all().count()
    cantproveedores = Proveedor.objects.all().count()
    cantdispositivos = Dispositivo.objects.all().count()
    cantdispositivos_asignados = Dispositivo.objects.filter(persona_asignada__isnull=False).count()
    cantdispositivos_no_asignados = cantdispositivos - cantdispositivos_asignados
    cantsoftwares = Software.objects.all().count()
    cantfacturas = Factura.objects.all().count()
    cantinventario = Inventario.objects.all().count()
    cantlicenciasregistradas = Licencia.objects.all().count()
    licencias = Software.objects.aggregate(totallic=Sum('cantidad_licencias'))
    cantLicenciasCompradas = licencias['totallic']
    context = {
        'parent': 'dashboard',
        'segment': 'dashboardv1',
        'cantPersonas': cantpersonas,
        'cantProveedores': cantproveedores,
        'cantDispositivos': cantdispositivos,
        'cantDispositivosAsignados': cantdispositivos_asignados,
        'cantDispositivosNoAsignados': cantdispositivos_no_asignados,
        'cantSoftwares': cantsoftwares,
        'cantlicenciasregistradas': cantlicenciasregistradas,
        'cantLicenciasCompradas': cantLicenciasCompradas,
        'cantFacturas': cantfacturas,
        'cantInventario': cantinventario,

    }
    return render(request, 'pages/index.html', context)
