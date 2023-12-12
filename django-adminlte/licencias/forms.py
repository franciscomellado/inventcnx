
from django.forms import ModelForm
from .models import Licencia
from django.forms import ( DateInput, DateField, Textarea)
class custom_form(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, DateField):
                field.widget = DateInput(
                    attrs={
                        "class": "form-control datepicker",
                        "data-toggle": "datetimepicker",
                        "data-target": "#id_" + field_name,
                    }
                )
        if field_name == "observacion":
            field.widget.attrs["rows"] = 5
                
class Licenciaform(custom_form):
    class Meta:
        model = Licencia
        exclude = ["fecha_activacion","fecha_vencimiento","asignada"]
        
        widgets = {
            "observaciones": Textarea(attrs={"cols": 80, "rows": 5}),
        }