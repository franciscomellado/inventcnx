from cProfile import label
from django.forms import ModelForm
from django.forms import (
    DateInput,
    DateField,
    Textarea,
    Select, BooleanField, CheckboxInput

)
from django.urls import reverse_lazy


from .models import Factura, Inventario, Dispositivo, Proveedor, Software
from licencias.models import Licencia
from django.contrib.contenttypes.forms import generic_inlineformset_factory
from django.forms import inlineformset_factory

class custom_form(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
        for field_name, field in self.fields.items():
            if isinstance(field, DateField):
                field.widget = DateInput(
                    attrs={
                        "class": "form-control datepicker",
                        "data-toggle": "datetimepicker",
                        "data-target": "#id_" + field_name,
                    }
                )
            if isinstance(field, BooleanField):
                field.widget = CheckboxInput(
                    attrs={
                        "class": "form-check-input",
                    }
                )
            if field_name == "observacion":
                field.widget.attrs["rows"] = 3

class Inventario_form(custom_form):
    class Meta:
        model = Inventario
        fields = "__all__"
        exclude = ("id",)
        widgets = {
            "observacion": Textarea(attrs={"cols": 80, "rows": 3}),
        }
# ---- Formulario de Dispositivo ---
class Dispositivo_form(custom_form):

    class Meta:
        model = Dispositivo
        fields = "__all__"
        widgets = {
            "observacion": Textarea(attrs={"cols": 80, "rows":3}),
        }
        
DispositivoInlineFormSet = generic_inlineformset_factory(
    Inventario,
    form=Dispositivo_form,
    fields="__all__",
    exclude = ("id", "fecha_caducidad"),
    can_delete=False,
    extra=1,
    
)

DispositivoInlineFormSetUpdate = generic_inlineformset_factory(
    Inventario,
    form=Dispositivo_form,
    fields="__all__",
    exclude =("id","fecha_caducidad"),
    can_delete=False,
    extra=0,
)

# ---- Formulario de Software ---
from licencias.forms import Licenciaform
class Software_form(custom_form):
    class Meta:
        model = Software
        fields = ['marca', 'version', 'fecha_instalacion', 'cuenta_asociada', 'cantidad_licencias']
        
      

class Proveedor_form(custom_form):
    class Meta:
        model = Proveedor
        fields = "__all__"
        
        
from django_addanother.widgets import AddAnotherWidgetWrapper     

class Factura_form(custom_form):
    class Meta:
        model = Factura
        fields = "__all__"
        widgets = {
                'proveedor': AddAnotherWidgetWrapper(
                    Select(attrs={'class': 'form-control select2'}, ),
                    reverse_lazy('inventario:crear_prove'),
                ),
            }
        
SoftwareInlineFormSet = generic_inlineformset_factory(
    Inventario,
    form = Software_form,
    fields = "__all__",
    exclude = ("id","fecha_caducidad",),
    can_delete=False,
    extra=0,
)

SoftwareInlineFormSetUpdate = generic_inlineformset_factory(
    Inventario,
    form = Software_form,
    fields = ("__all__"),
    exclude = ("id", "fecha_caducidad",),
    can_delete=False,
    extra=1,
)
        
# LicenciaFormSet = inlineformset_factory(
#     Software,  # Modelo padre
#     Licencia,  # Modelo hijo
#     fields=('nombre', 'numero_identificacion', 'tipo_licencia', 'observacion', 'estado'),  # Campos a mostrar en el formulario
#     extra=1, # Número inicial de formularios en línea
#     exclude = ["id"]
# )

# class SoftwarelicenciaForm(custom_form):
#     class Meta:
#         model = Software
#         fields = ['marca', 'version', 'fecha_instalacion', 'cuenta_asociada', ]
