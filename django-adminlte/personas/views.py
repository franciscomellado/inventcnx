from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Personas, Area, Departamento
from django.urls import reverse_lazy
from .forms import *
from django.contrib import messages

class PersonasListView(LoginRequiredMixin,ListView):
    model: Personas
    queryset= Personas.objects.all()
    template_name = 'personas/personas_list.html'
    
class PersonasCreateView(SuccessMessageMixin, CreateView):
    model: Personas
    form_class = Personas_form
    template_name = 'personas/personas_form.html'
    success_url = reverse_lazy("personas:index")
    success_message = "  %(nombre)s ha sido creado con exito"
    
class PersonasDeleteView(SuccessMessageMixin,DeleteView):
    model = Personas
    success_url = reverse_lazy("personas:index")
    success_message = "%(nombre)s ha sido eliminado exitosamente"
    
    
    
class PersonasUpdateView(SuccessMessageMixin,UpdateView):
    model = Personas
    form_class = Personas_form
    template_name = "personas/personas_update_form.html"
    success_message = " Actualización realizada con exito de %(nombre)s "
    
    
# Areas  
class AreaListView(LoginRequiredMixin,ListView):
    model: Area
    queryset= Area.objects.all()
    template_name = 'personas/area/area_list.html'
    
class AreaCreateView(CreateView):
    model: Area
    form_class = Area_form
    template_name = 'personas/area/area_form.html'
    success_url = reverse_lazy("personas:area")
    
class AreaDeleteView(DeleteView):
    model = Area
    template_name = 'personas/area/area_confirm_delete.html'
    def get_success_url(self):
        messages.success(self.request, "Eliminado exitosamente")
        return reverse_lazy("personas:area")
    
class AreaUpdateView(UpdateView):
    model = Area
    form_class = Area_form
    template_name = "personas/area/area_update_form.html"
    success_url = reverse_lazy("personas:area")
    
    # Departamento   
class DepartamentoListView(LoginRequiredMixin,ListView):
    model: Departamento
    queryset= Departamento.objects.all()
    template_name = 'personas/dpto/departamento_list.html'
    
class DepartamentoCreateView(CreateView):
    model: Departamento
    form_class = Departamento_form
    template_name = 'personas/dpto/departamento_form.html'
    success_url = reverse_lazy("personas:departamento")
    
class DepartamentoDeleteView(DeleteView):
    model = Departamento
    template_name = 'personas/dpto/departamento_confirm_delete.html'
    def get_success_url(self):
        messages.success(self.request, "Eliminado exitosamente")
        return reverse_lazy("personas:departamento")
    
