from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect, render
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
    template_name = "personas/personas_confirm_delete.html"
    success_url = reverse_lazy("personas:index")
    success_message = "La persona ha sido eliminado exitosamente"


class PersonasUpdateView(SuccessMessageMixin, UpdateView):
    model = Persona
    form_class = Personas_form
    template_name = "personas/personas_update_form.html"
    success_url = reverse_lazy("personas:index")
    success_message = " Actualización realizada con exito de %(nombre)s "

    # Departamento
class DepartamentoListView(LoginRequiredMixin, ListView):
    model: Departamento
    queryset = Departamento.objects.all()
    template_name = "personas/dpto/departamento_list.html"
    

class DepartamentoCreateView(SuccessMessageMixin,CreateView):
    model: Departamento
    form_class = Departamento_form
    template_name = "personas/dpto/departamento_form.html"
    success_message = " La gerencia ha sido creada con exito"
    success_url = reverse_lazy("personas:dpto")


class DepartamentoDeleteView(SuccessMessageMixin,DeleteView):
    model = Departamento
    template_name = "personas/dpto/departamento_confirm_delete.html"
    success_url = reverse_lazy("personas:dpto")
    success_message = "La gerencia ha sido eliminado exitosamente"
    
    def post(self, request, *args, **kwargs):
        gerencia = self.get_object() # Verificar si el departamento tiene personas asociadas
        if Departamento.objects.filter(gerencia=gerencia).exists():
            # Si tiene personas asociadas, mostrar un mensaje de advertencia y cancelar la operación de eliminación
            messages.add_message(self.request, messages.WARNING, "El departamento tiene personas asociadas. No puede eliminarlo.")
            return HttpResponseRedirect(self.success_url)
        # Si no tiene facturas asociadas, eliminar el proveedor y redirigir a la lista de facturas
        return super().post(request, *args, **kwargs)


class DepartamentoUpdateView(SuccessMessageMixin,UpdateView):
    model = Departamento
    form_class = Departamento_form
    template_name = "personas/dpto/departamento_update_form.html"
    success_url = reverse_lazy("personas:dpto")
    success_message = "La gerencia ha sido actualizada exitosamente"
