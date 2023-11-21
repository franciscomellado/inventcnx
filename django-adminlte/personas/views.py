from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import *
from .models import  Departamento, Persona


class PersonasListView(LoginRequiredMixin, ListView):
    model: Persona
    queryset = Persona.objects.all()
    template_name = "personas/personas_list.html"


class PersonasCreateView(SuccessMessageMixin, CreateView):
    model: Persona
    form_class = Personas_form
    template_name = "personas/personas_form.html"
    success_url = reverse_lazy("personas:index")
    success_message = "  %(nombre)s ha sido creado con exito"


class PersonasDeleteView(SuccessMessageMixin, DeleteView):
    model = Persona
    success_url = reverse_lazy("personas:index")
    success_message = "%(nombre)s ha sido eliminado exitosamente"


class PersonasUpdateView(SuccessMessageMixin, UpdateView):
    model = Persona
    form_class = Personas_form
    template_name = "personas/personas_update_form.html"
    success_message = " Actualización realizada con exito de %(nombre)s "

    # Departamento
class DepartamentoListView(LoginRequiredMixin, ListView):
    model: Departamento
    queryset = Departamento.objects.all()
    template_name = "personas/dpto/departamento_list.html"

class DepartamentoCreateView(CreateView):
    model: Departamento
    form_class = Departamento_form
    template_name = "personas/dpto/departamento_form.html"
    success_url = reverse_lazy("personas:dpto")


class DepartamentoDeleteView(DeleteView):
    model = Departamento
    template_name = "personas/dpto/departamento_confirm_delete.html"

    def get_success_url(self):
        messages.success(self.request, "Eliminado exitosamente")
        return reverse_lazy("personas:dpto")


class DepartamentoUpdateView(UpdateView):
    model = Departamento
    form_class = Departamento_form
    template_name = "personas/dpto/departamento_update_form.html"
    success_url = reverse_lazy("personas:dpto")
