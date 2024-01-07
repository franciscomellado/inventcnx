from datetime import date, timedelta
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ExpressionWrapper, F, fields
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_addanother.views import UpdatePopupMixin

from .forms import *
from .models import Dispositivo, Factura, Inventario, Proveedor, Software


def annotate_inventory_fields(queryset):
    queryset = queryset.annotate(
            nombre_inventario=F('inventario__nombre'),
            valor_inventario=F('inventario__valor'),
            disponible_inventario =F('inventario__disponible'),
            duracion_inventario =F('inventario__duracion'),
            estado_inventario =F('inventario__estado__estado'),
            fecha_registro_inventario =F('inventario__fecha_registro'),
            fecha_entrega_inventario =F('inventario__fecha_entrega'),
            fecha_caducidad_inventario=F('inventario__fecha_caducidad'),
            observacion_inventario =F('inventario__observacion'),
            #factura
            factura_inventario = F('inventario__factura__factura'),
            fecha_registro_factura_inventario = F('inventario__factura__fecha_factura'),
            fecha_factura_inventario = F('inventario__factura__fecha_registro'),
            proveedor_factura_inventario = F('inventario__factura__proveedor__nombre'),
            orden_de_compra_inventario = F('inventario__factura__orden_de_compra'),
            #otras
            tiempo_de_vida_inventario=ExpressionWrapper( date.today() -
                F('inventario__factura__fecha_factura'),
                output_field=fields.DurationField()
            ),        
    )
    return queryset

class InventarioListViews(SuccessMessageMixin,ListView):
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
    success_url = reverse_lazy("inventario:index")
    template_name = "inventario/inventario_update_form.html"
    success_message = " ha sido actualizado con exito."

class InventarioDeleteView(SuccessMessageMixin,DeleteView):
    model= Inventario
    success_url = reverse_lazy("inventario:index")
    template_name = "inventario/inventario_delete.html"
    success_message = "%(nombre) ha sido eliminado exitosamente."
    
########################### ---- Vistas para Dispositivos -----    
class DispositivoListViews(LoginRequiredMixin,ListView):
    models: Dispositivo
    queryset = Dispositivo.objects.all()
    template_name = 'dispositivo/dispositivo_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = annotate_inventory_fields(queryset)
        return queryset

class DispositivoCardsListViews(LoginRequiredMixin,ListView):
    models: Dispositivo
    queryset = Dispositivo.objects.all()
    template_name = 'dispositivo/dispositivo_list_cards.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = annotate_inventory_fields(queryset)
        return queryset
 

class DispositivoCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model= Dispositivo
    template_name = "dispositivo/dispositivo_form.html"
    form_class = Dispositivo_form
    formset = DispositivoInlineFormSet
    success_url = reverse_lazy("inventario:index_disp")
    success_message = "%(modelo)s ha sido creado con exito."
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            formset = DispositivoInlineFormSet(self.request.POST)
        else:
            formset = DispositivoInlineFormSet()
        context['formset'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            self.object.tipo='H'
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))
    
    
class DispositivoUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Dispositivo
    form_class = Dispositivo_form
    success_url = reverse_lazy("inventario:index_disp")
    template_name = "dispositivo/dispositivo_update_form.html"
    success_message = "Ha sido actualizado con exito."
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = DispositivoInlineFormSetUpdate(instance = self.object)
        return self.render_to_response(self.get_context_data(form = form, formset = formset))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = DispositivoInlineFormSet(self.request.POST, instance=self.object)
        if (form.is_valid() and formset.is_valid()):
            return self.form_valid(form, formset)
        return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset_disp=formset))
    
class DispositivoDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model= Dispositivo
    success_url = reverse_lazy("inventario:index_disp")
    template_name = "dispositivo/dispositivo_confirm_delete.html"
    success_message = " Ha sido eliminado exitosamente."
    
    
class DispositivoDetailView(LoginRequiredMixin,DetailView):
    model = Dispositivo
    template_name = "dispositivo/dispositivo_detail.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = annotate_inventory_fields(queryset)
        return queryset

########################### ---- Vistas para Software -----    
class SoftwareListViews(LoginRequiredMixin,SuccessMessageMixin,ListView):
    models: Software
    queryset = Software.objects.all()
    template_name = 'software/software_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = annotate_inventory_fields(queryset)
        return queryset
    
class SoftwareCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model= Software
    template_name = "software/software_form.html"
    form_class = Software_form
    formset = SoftwareInlineFormSet
    success_url = reverse_lazy("inventario:index_soft")
    success_message = "Ha sido creado con exito."
    
    def get_context_data(self, **kwargs):
        context = super(SoftwareCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['inventario_formset']= SoftwareInlineFormSet(self.request.POST)
        else:
            context['inventario_formset'] = SoftwareInlineFormSetUpdate()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        inventario_formset = context['inventario_formset']
        if inventario_formset.is_valid():
            self.object = form.save()
            inventario_formset.instance = self.object
            inventario_formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))
    
class SoftwareUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Software
    form_class = Software_form
    success_url = reverse_lazy("inventario:index_soft")
    template_name = "software/software_update_form.html"
    success_message = "Ha sido actualizado con exito."
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = SoftwareInlineFormSet(instance = self.object)
        return self.render_to_response(self.get_context_data(form = form, formset = formset))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = SoftwareInlineFormSet(self.request.POST, instance=self.object)

        if (form.is_valid() and formset.is_valid()):
            return self.form_valid(form, formset)
        return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset_disp=formset))

class SoftwareDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model= Software
    success_url = reverse_lazy("inventario:index_soft")
    template_name = "software/software_confirm_delete.html"
    success_message = "Ha sido eliminado exitosamente."
    


########################### ---- Vistas para Proveedor -----  
class ProveedorListViews(LoginRequiredMixin,ListView):
    models = Proveedor
    queryset = Proveedor.objects.all()
    template_name = 'proveedor/proveedor_list.html'
    
from django_addanother.views import CreatePopupMixin,UpdatePopupMixin
class ProveedorCreateView(LoginRequiredMixin,SuccessMessageMixin,CreatePopupMixin,CreateView):
    model= Proveedor
    form_class = Proveedor_form
    template_name = "proveedor/proveedor_form.html"
    success_url = reverse_lazy("inventario:index_prove")
    success_message = "%(nombre)s ha sido creado con exito."
    
class ProveedorUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdatePopupMixin,UpdateView):
    model = Proveedor
    form_class = Proveedor_form
    success_url = reverse_lazy("inventario:index_prove")
    template_name = "proveedor/proveedor_update_form.html"
    success_message = "%(nombre)s ha sido actualizado con exito."

class ProveedorDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model= Proveedor
    success_url = reverse_lazy("inventario:index_prove")
    template_name = "proveedor/proveedor_confirm_delete.html"
    success_message = "El Proveedor ha sido eliminado exitosamente."
    
    def post(self, request, *args, **kwargs):
        # Verificar si el proveedor tiene facturas asociadas
        proveedor = self.get_object()
        if Factura.objects.filter(proveedor=proveedor).exists():
            # Si tiene facturas asociadas, mostrar un mensaje de advertencia y cancelar la operación de eliminación
            messages.add_message(self.request, messages.WARNING, "El proveedor tiene facturas asociadas. No puede eliminarlo.")
            return HttpResponseRedirect(self.success_url)
        # Si no tiene facturas asociadas, eliminar el proveedor y redirigir a la lista de facturas
        return super().post(request, *args, **kwargs)

    
########################### Factura ###########
    
class FacturaListViews(LoginRequiredMixin,SuccessMessageMixin,ListView):
    model= Factura
    queryset = Factura.objects.all()
    template_name = 'factura/factura_list.html'
    
class FacturaCreateView(LoginRequiredMixin,SuccessMessageMixin,CreatePopupMixin,CreateView):
    model = Factura
    form_class = Factura_form
    template_name = "factura/factura_form.html"
    success_url = reverse_lazy("inventario:index_factu")
    success_message = "%(factura)s ha sido creado con exito."
    
class FacturaUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdatePopupMixin ,UpdateView):
    model = Factura
    form_class = Factura_form
    success_url = reverse_lazy("inventario:index_factu")
    template_name = "factura/factura_update_form.html"
    success_message = " ha sido actualizado con exito."

class FacturaDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model= Factura
    success_url = reverse_lazy("inventario:index_factu")
    template_name = "factura/factura_confirm_delete.html"
    success_message = "La factura sido eliminado exitosamente."

class AvisosVencimientoView(View):
    def get(self, request):
        dispositivos = Dispositivo.objects.filter(fecha_caducidad__gte=date.today(), fecha_caducidad__lte=date.today() + timedelta(days=30))
        software = Software.objects.filter(fecha_caducidad__gte=date.today(), fecha_caducidad__lte=date.today() + timedelta(days=30))
        return render(request, 'avisos.html', {'dispositivos': dispositivos, 'software': software})
    