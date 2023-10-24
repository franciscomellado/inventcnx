from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import *
from .models import Persona


class PersonasListView(ListView):
    model= Persona
    queryset = Persona.objects.all()
    template_name = "personas/personas_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class PersonasCreateView(CreateView):
    model= Persona
    form_class = Personas_form
    template_name = "personas/personas_form.html"
    success_url = reverse_lazy("personas:index")
    success_message = "%(nombre)s ha sido creado con exito."


class PersonasUpdateView(UpdateView):
    model = Persona
    form_class = Personas_form
    success_url = reverse_lazy("personas:index")
    template_name = "personas/personas_update_form.html"

class PersonasDeleteView( DeleteView):
    model= Persona
    success_url = reverse_lazy("personas:index")
    template_name = "personas/personas_delete.html"
    success_message = "%(nombre) ha sido eliminado exitosamente."
