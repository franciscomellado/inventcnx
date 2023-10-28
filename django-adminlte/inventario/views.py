from django.shortcuts import render
from django.views.generic import ListView
from .models import Inventario
from .forms import Inventario_form, InventarioInlineFormSet
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

class InventarioListViews(ListView):
    models: Inventario
    queryset = Inventario.objects.all()
    template_name = 'inventario/inventario_list.html'
    
    
class InventarioCreateView(SuccessMessageMixin,CreateView):
    model= Inventario
    template_name = "inventario/inventario_form.html"
    success_url = reverse_lazy("inventario:index")
    success_message = "%(nombre)s ha sido creado con exito."
    
class InventarioUpdateView(SuccessMessageMixin,UpdateView):
    model = Inventario
    form_class = Inventario_form
    #inline_model = Inventario
    formset = InventarioInlineFormSet
    
    success_url = reverse_lazy("inventario:index")
    template_name = "inventario/inventario_update_form.html"
    success_message = "%(nombre)s ha sido actualizado con exito."

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.formset = self.formset(instance=self.object)
        print(self.formset)
        return super().dispatch(request, *args, **kwargs)
class InventarioDeleteView(SuccessMessageMixin,DeleteView):
    model= Inventario
    success_url = reverse_lazy("inventario:index")
    template_name = "inventario/inventario_delete.html"
    success_message = "%(nombre) ha sido eliminado exitosamente."