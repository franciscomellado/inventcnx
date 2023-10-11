from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Usuario

class Personaindex(TemplateView):
    template_name = 'personas/data.html'
    
def tablapersona(request):
    listar_persona = Usuario.objects.all()
    data = {
        'listar_persona': listar_persona,
    }
    return render(request, 'listar_persona.html', data)
