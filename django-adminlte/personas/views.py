from audioop import reverse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Personas
from django.urls import reverse_lazy
from .forms import Personas_form
from django.contrib import messages

class PersonasListView(LoginRequiredMixin,ListView):
    model: Personas
    queryset= Personas.objects.all()
    template_name = 'personas/personas_list.html'
    
class PersonascreateView(CreateView):
    model: Personas
    form_class = Personas_form
    template_name = 'personas/personas_form.html'
    success_url = reverse_lazy("personas:index")
    
class PersonasDeleteView(DeleteView):
    model = Personas
    def get_success_url(self):
        messages.success(self.request, "Eliminado exitosamente")
        return reverse_lazy("personas:index")
    

class PersonasUpdateView(UpdateView):
    model = Personas
    fields = ["nombre","apellido","email", "area", "departamento"]
    template_name = "personas/personas_update_form.html"
    success_url = reverse_lazy("personas:index")
