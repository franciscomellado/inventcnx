from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from .models import Persona

# class Personaindex(TemplateView):
#     template_name = 'personas/data.html'
    
# def tablapersona(request):
#     listar_persona = Usuario.objects.all()
#     data = {
#         'listar_persona': listar_persona,
#     }
#     return render(request, 'listar_persona.html', data)

class PersonaListWiews(ListView):
    models: Persona
    queryset = Persona.objects.all()
    template_name = 'personas/personas_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    
    