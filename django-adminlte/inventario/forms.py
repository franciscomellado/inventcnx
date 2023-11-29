from django.forms import ModelForm
from django.forms import (
    DateInput,
    DateField,
    ImageField,
    FileInput,
    ClearableFileInput,
)
from .models import Factura, Inventario, Dispositivo, Proveedor, Software
from django.contrib.contenttypes.forms import generic_inlineformset_factory


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

class Inventario_form(custom_form):
    class Meta:
        model = Inventario
        fields = "__all__"
        
# ---- Formulario de Dispositivo ---
class Dispositivo_form(custom_form):

    class Meta:
        model = Dispositivo
        fields = "__all__"
        
DispositivoInlineFormSet = generic_inlineformset_factory(
    Inventario,
    form=Dispositivo_form,
    fields="__all__",
    exclude = [ "fecha_caducidad"],
    can_delete=False,
    extra=1,
)

DispositivoInlineFormSetUpdate = generic_inlineformset_factory(
    Inventario,
    form=Dispositivo_form,
    fields="__all__",
    exclude = ["fecha_caducidad"],
    can_delete=False,
    extra=0,
)

# ---- Formulario de Software ---
class Software_form(custom_form):
    class Meta:
        model = Software
        fields = "__all__"
        exclude = ["id"]


SoftwareInlineFormSet = generic_inlineformset_factory(
    Inventario,
    form = Software_form,
    fields = "__all__",
    exclude = [ "fecha_caducidad",],
    can_delete=False,
    extra=1,
)

SoftwareInlineFormSetUpdate = generic_inlineformset_factory(
    Inventario,
    form = Software_form,
    fields = "__all__",
    exclude = [ "fecha_caducidad",],
    can_delete=False,
    extra=0,
)

class Proveedor_form(custom_form):
    class Meta:
        model = Proveedor
        fields = '__all__'
        
class Factura_form(custom_form):
    class Meta:
        model = Factura
        fields = '__all__'
    