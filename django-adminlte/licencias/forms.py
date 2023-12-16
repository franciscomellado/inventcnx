
from django.forms import ModelForm
from .models import Licencia,LicenciaUsuario
from django.forms import ( DateInput, DateField, Textarea, Select)
class custom_form(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, DateField):
                field.widget = DateInput(
                    attrs={
                        "class": "datepicker",
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
            "software": Select(attrs={
                "class":"select2",
                }),
        }
   
        
class LicenciaUsuarioform(custom_form):
    class Meta:
        model = LicenciaUsuario
        exclude = ["fecha_registro","creado_por"]
        
        widgets = {
            "observaciones": Textarea(attrs={"cols": 80, "rows": 5}),
            "persona": Select(attrs={"class":"select2", "style": "width: 100%"}),
            "licencia": Select(attrs={"class":"select2", "style": "width: 100%", "disabled": "true" }),
        
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['licencia'].queryset = Licencia.objects.none()