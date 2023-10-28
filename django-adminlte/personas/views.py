from django.contrib.messages.views import SuccessMessageMixin
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


class PersonasCreateView(CreateView, SuccessMessageMixin):
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

class PersonasDeleteView(DeleteView,SuccessMessageMixin):
    model= Persona
    success_url = reverse_lazy("personas:index")
    template_name = "personas/personas_delete.html"
    success_message = "%(nombre) ha sido eliminado exitosamente."
