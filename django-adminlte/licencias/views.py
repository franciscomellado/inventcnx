from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import *
from .models import  Licencia

class LicenciasListView(LoginRequiredMixin, ListView):
    model: Licencia
    queryset = Licencia.objects.all()
    template_name = "licencia/licencia_list.html"

class LicenciasCreateView(SuccessMessageMixin, CreateView):
    model: Licencia
    form_class = Licenciaform
    template_name = "licencia/licencia_form.html"
    success_url = reverse_lazy("licencias:index")
    success_message = "  %(nombre)s ha sido creado con exito"
    
    def get_queryset(self):
        super().get_queryset()
        
        return 
    

class LicenciassDeleteView(SuccessMessageMixin, DeleteView):
  model = Licencia
  template_name = "licencia/licencia_confirm_delete.html"
  success_url = reverse_lazy("licencia:index")
  success_message = "La persona ha sido eliminado exitosamente"
  
# keyword 'licencia' into field. Choices are: disponible, estado, estado_id, fecha_activacion, fecha_vencimiento, id, nombre, numero_identificacion, observacion, personasAsig, software, software_id, tipo_licencia, tipo_licencia_id, usuarios_asignados

  def post(self, request, *args, **kwargs):
        licencia = self.get_object() # 
        if Licencia.objects.filter(licencia=licencia).exists():
            # Si tiene personas asociadas, mostrar un mensaje de advertencia y cancelar la operación de eliminación
            messages.add_message(self.request, messages.WARNING, "La licencia tiene personas asociadas. No puede eliminarlo.")
            return HttpResponseRedirect(self.success_url)
        # Si no tiene facturas asociadas, eliminar el proveedor y redirigir a la lista de facturas
        return super().post(request, *args, **kwargs)
class LicenciasUpdateView(SuccessMessageMixin, UpdateView):
    model = Licencia
    form_class = Licenciaform
    template_name = "licencia/licencia_update_form.html"
    success_url = reverse_lazy("licencias:index")
    success_message = " Actualización realizada con exito de %(nombre)s "
