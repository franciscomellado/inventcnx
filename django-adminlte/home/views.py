from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from inventario.models import Proveedor
from personas.models import Persona


# Create your views here.
@login_required
def index(request):
    cantpersonas = Persona.objects.all().count()
    cantproveedores = Proveedor.objects.all().count()
    context = {
        'parent': 'dashboard',
        'segment': 'dashboardv1',
        'cantPersonas': cantpersonas,
        'cantProveedores': cantproveedores,

    }
    return render(request, 'pages/index.html', context)
