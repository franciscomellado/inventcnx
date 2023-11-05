from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from personas.models import Persona


# Create your views here.
@login_required
def index(request):
    
    cantpersonas = Persona.objects.all().count()
    context = {
        'parent': 'dashboard',
        'segment': 'dashboardv1',
        'cantPersonas': cantpersonas

    }
    return render(request, 'pages/index.html', context)
