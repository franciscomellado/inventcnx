from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from inventario.models import Proveedor, Dispositivo,Software,Factura,Inventario
from personas.models import Persona


# Create your views here.
@login_required
def index(request):
    cantpersonas = Persona.objects.all().count()
    cantproveedores = Proveedor.objects.all().count()
    cantdispositivos = Dispositivo.objects.all().count()
    cantdispositivos_asignados = Dispositivo.objects.filter(inventario__persona_asignada__isnull=False).count()
    cantdispositivos_no_asignados = cantdispositivos - cantdispositivos_asignados
    cantsoftwares = Software.objects.all().count()
    cantsoftwares_asignados = Software.objects.filter(inventario__persona_asignada__isnull=False).count()
    cantsoftwares_no_asignados = cantsoftwares - cantsoftwares_asignados
    cantfacturas = Factura.objects.all().count()
    cantinventario = Inventario.objects.all().count()
    context = {
        'parent': 'dashboard',
        'segment': 'dashboardv1',
        'cantPersonas': cantpersonas,
        'cantProveedores': cantproveedores,
        'cantDispositivos': cantdispositivos,
        'cantDispositivosAsignados': cantdispositivos_asignados,
        'cantDispositivosNoAsignados': cantdispositivos_no_asignados,
        'cantSoftwares': cantsoftwares,
        'cantSoftwaresAsignados': cantsoftwares_asignados,
        'cantSoftwaresNoAsignados': cantsoftwares_no_asignados,
        'cantFacturas': cantfacturas,
        'cantInventario': cantinventario,

    }
    return render(request, 'pages/index.html', context)
