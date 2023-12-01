from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView
from .models import Inventario, Dispositivo, Software, Proveedor, Factura
from .forms import *
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import F,Case,When
from datetime import date, timedelta
from django.shortcuts import render
from django.views import View
from django.conf import settings
import os


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
    
####---- Vistas para Dispositivos -----    
class DispositivoListViews(SuccessMessageMixin,ListView):
    models: Dispositivo
    queryset = Dispositivo.objects.all()
    template_name = 'dispositivo/dispositivo_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(
            nombre_inventario=F('inventario__nombre'),
            valor_inventario=F('inventario__valor'),
            disponible_inventario =F('inventario__disponible'),
            estado_inventario =F('inventario__estado__estado'),
            fecha_registro_inventario =F('inventario__fecha_registro'),
            fecha_entrega_inventario =F('inventario__fecha_entrega'),
            fecha_caducidad_inventario=F('inventario__fecha_caducidad'),
            proveedor_inventario =F('inventario__proveedor__nombre'),
            factura_inventario = F('inventario__factura__factura'),
            persona_nombre_inventario=F('inventario__persona_asignada__nombre'),
            persona_apellido_inventario=F('inventario__persona_asignada__apellido'),
            gerencia_inventario_nombre=F('inventario__persona_asignada__gerencia__gerencia'),
        )
        return queryset

class DispositivoCardsListViews(SuccessMessageMixin,ListView):
    models: Dispositivo
    queryset = Dispositivo.objects.all()
    template_name = 'dispositivo/dispositivo_list_cards.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(
            nombre_inventario=F('inventario__nombre'),
            valor_inventario=F('inventario__valor'),
            disponible_inventario =F('inventario__disponible'),
            estado_inventario =F('inventario__estado__estado'),
            fecha_registro_inventario =F('inventario__fecha_registro'),
            fecha_entrega_inventario =F('inventario__fecha_entrega'),
            fecha_caducidad_inventario=F('inventario__fecha_caducidad'),
            proveedor_inventario =F('inventario__proveedor__nombre'),
            factura_inventario = F('inventario__factura__factura'),
            persona_nombre_inventario=F('inventario__persona_asignada__nombre'),
            persona_apellido_inventario=F('inventario__persona_asignada__apellido'),
            gerencia_inventario_nombre=F('inventario__persona_asignada__gerencia__gerencia'),
        )
        return queryset
 

class DispositivoCreateView(SuccessMessageMixin,CreateView):
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
    
    
class DispositivoUpdateView(SuccessMessageMixin,UpdateView):
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
    
class DispositivoDeleteView(SuccessMessageMixin,DeleteView):
    model= Dispositivo
    success_url = reverse_lazy("inventario:index_disp")
    template_name = "dispositivo/dispositivo_delete.html"
    success_message = " Ha sido eliminado exitosamente."
    
    def delete(self, request, *args, **kwargs):
        # Obtener la instancia del dispositivo a eliminar
        dispositivo = self.get_object()
        # Eliminar el archivo de imagen asociado al dispositivo
        if dispositivo.imagen_dispostivo:
            os.remove(os.path.join(settings.MEDIA_ROOT, dispositivo.imagen_dispostivo.name))

        # Eliminar la instancia del dispositivo
        return super().delete(request, *args, **kwargs)
    
class DispositivoDetailView(DetailView):
    model = Dispositivo
    template_name = "dispositivo/dispositivo_detail.html"
    


####---- Vistas para Software -----    
class SoftwareListViews(SuccessMessageMixin,ListView):
    models: Software
    queryset = Software.objects.all()
    template_name = 'software/software_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(
            nombre_inventario=F('inventario__nombre'),
            valor_inventario=F('inventario__valor'),
            cantidad_licencias = F('inventario__factura__cantidad_licencias'),
            duracion = F('inventario__duracion'),
            disponible_inventario =F('inventario__disponible'),
            estado_inventario =F('inventario__estado__estado'),
            fecha_compra = F('inventario__factura__fecha_factura'),
            fecha_caducidad = F('inventario__fecha_caducidad'),
            factura_inventario = F('inventario__factura__factura'),
            persona_nombre_inventario=F('inventario__persona_asignada__nombre'),
            persona_apellido_inventario=F('inventario__persona_asignada__apellido'),
            gerencia_inventario_nombre=F('inventario__persona_asignada__gerencia__gerencia'),
        )
        return queryset
    
class SoftwareCreateView(SuccessMessageMixin,CreateView):
    model= Software
    template_name = "software/software_form.html"
    form_class = Software_form
    formset = SoftwareInlineFormSet
    success_url = reverse_lazy("inventario:index_soft")
    success_message = "Ha sido creado con exito."
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            formset = SoftwareInlineFormSetUpdate(self.request.POST)
        else:
            formset = SoftwareInlineFormSet()
        context['formset'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            self.object.tipo='S'
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))
    
class SoftwareUpdateView(SuccessMessageMixin,UpdateView):
    model = Software
    form_class = Software_form
    success_url = reverse_lazy("inventario:index_soft")
    template_name = "software/software_update_form.html"
    success_message = "Ha sido actualizado con exito."
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = SoftwareInlineFormSetUpdate(instance = self.object)
        return self.render_to_response(self.get_context_data(form = form, formset = formset))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = SoftwareInlineFormSetUpdate(self.request.POST, instance=self.object)

        if (form.is_valid() and formset.is_valid()):
            return self.form_valid(form, formset)
        return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        if 'fecha_compra' in formset.changed_data:
            formset.fecha_caducidad = formset.fecha_compra + timedelta(years=int(formset.duracion))
        formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset_disp=formset))

class SoftwareDeleteView(SuccessMessageMixin,DeleteView):
    model= Software
    success_url = reverse_lazy("inventario:index_soft")
    template_name = "software/software_delete.html"
    success_message = "Ha sido eliminado exitosamente."
    
####---- Vistas para Proveedor -----  
class ProveedorListViews(ListView):
    models = Proveedor
    queryset = Proveedor.objects.all()
    template_name = 'proveedor/proveedor_list.html'
class ProveedorCreateView(SuccessMessageMixin,CreateView):
    model= Proveedor
    form_class = Proveedor_form
    template_name = "proveedor/proveedor_form.html"
    success_url = reverse_lazy("inventario:index_prove")
    success_message = "%(nombre)s ha sido creado con exito."
    
class ProveedorUpdateView(SuccessMessageMixin,UpdateView):
    model = Proveedor
    form_class = Proveedor_form
    success_url = reverse_lazy("inventario:index_prove")
    template_name = "proveedor/proveedor_update_form.html"
    success_message = "%(nombre)s ha sido actualizado con exito."

class ProveedorDeleteView(SuccessMessageMixin,DeleteView):
    model= Proveedor
    success_url = reverse_lazy("inventario:index_prove")
    template_name = "proveedor/proveedor_delete.html"
    success_message = "%(nombre)s ha sido eliminado exitosamente."
    

class AvisosVencimientoView(View):
    def get(self, request):
        dispositivos = Dispositivo.objects.filter(fecha_caducidad__gte=date.today(), fecha_caducidad__lte=date.today() + timedelta(days=30))
        software = Software.objects.filter(fecha_caducidad__gte=date.today(), fecha_caducidad__lte=date.today() + timedelta(days=30))
        return render(request, 'avisos.html', {'dispositivos': dispositivos, 'software': software})
    
    
    ##### Factura ###########
    
class FacturaListViews(SuccessMessageMixin,ListView):
    model= Factura
    queryset = Factura.objects.all()
    template_name = 'factura/factura_list.html'
class FacturaCreateView(SuccessMessageMixin,CreateView):
    model = Factura
    form_class = Factura_form
    template_name = "factura/factura_form.html"
    success_url = reverse_lazy("inventario:index")
    success_message = "%(factura)s ha sido creado con exito."
    
class FacturaUpdateView(SuccessMessageMixin,UpdateView):
    model = Factura
    form_class = Factura_form
    success_url = reverse_lazy("inventario:index_factu")
    template_name = "factura/factura_update_form.html"
    success_message = " ha sido actualizado con exito."

class FacturaDeleteView(SuccessMessageMixin,DeleteView):
    model= Factura
    success_url = reverse_lazy("inventario:index")
    template_name = "factura/factura_delete.html"
    success_message = "%(factura) ha sido eliminado exitosamente."