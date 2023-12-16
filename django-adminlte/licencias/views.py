from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import *
from .models import  Licencia,LicenciaUsuario
from personas.models import Persona
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
class LicenciasListView(LoginRequiredMixin, ListView):
    model: Licencia
    queryset = Licencia.objects.all()
    template_name = "licencia/licencia_list.html"
    

class LicenciasCreateView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    model: Licencia
    form_class = Licenciaform
    template_name = "licencia/licencia_form.html"
    success_url = reverse_lazy("licencias:index")
    success_message = "  %(nombre)s ha sido creado con exito"
    
    def get_queryset(self):
        super().get_queryset()
        
        return 
    

class LicenciassDeleteView(LoginRequiredMixin,SuccessMessageMixin, DeleteView):
  model = Licencia
  template_name = "licencia/licencia_confirm_delete.html"
  success_url = reverse_lazy("licencias:index")
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

    
class AsignarLicenciasView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = LicenciaUsuario
    form_class = LicenciaUsuarioform
    template_name = "licencia/licenciausuario_form.html"
    success_url = reverse_lazy("licencias:index")
    success_message = " Asignación de licencia a usuario ha sidorealizada con exito "
    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        # request.is_ajax() is deprecated since django 3.1
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            data = {}
            try:
                action = request.POST['action']
                persona_id = request.POST['id']
                if action == 'getLicenciasPersona':
                    data = []
                    for i in Licencia.objects.filter(asignada=False):
                            data.append({'id': i.pk, 'nombre': i.nombre})
                else:
                    data['error'] = 'Ha ocurrido un error'
            except Exception as e:
                data['error'] = str(e)
            return JsonResponse(data, safe=False)
        else:
            return super().post(request, *args, **kwargs)