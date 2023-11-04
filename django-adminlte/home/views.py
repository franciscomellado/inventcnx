from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from personas.models import Personas


# Create your views here.
@login_required
def index(request):
    
    cantpersonas = Personas.objects.all().count()
    context = {
        'parent': 'dashboard',
        'segment': 'dashboardv1',
        'cantPersonas': cantpersonas

    }
    print(context)
    return render(request, 'pages/index.html', context)
