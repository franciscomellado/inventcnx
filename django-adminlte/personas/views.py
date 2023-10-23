from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from .models import Persona
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import *
from django.contrib import messages

class PersonasListWiews(ListView):
    models: Persona
    queryset = Persona.objects.all()
    template_name = 'personas/personas_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class PersonasCreateViews(CreateView):
    models: Persona
    form_class = Personas_form
    template_name = 'personas/personas_form.html'
    success_url = reverse_lazy("personas:index")
    success_message = "%(nombre)s ha sido creado con exito."

class PersonasUpdateViews(UpdateView): # editar
    models: Persona
    form_class = Personas_form
    success_url =  reverse_lazy("personas:editar")
    template_name = 'personas/personas_update_form.html'
    success_url = "Actualización realizada con exito de %(nombre)s."

class PersonasDeleteWiews(ListView,DeleteView):
    models: Persona
    success_url =  reverse_lazy("personas:index")
    success_message = "%(nombre) ha sido eliminado exitosamente."


    

    
    