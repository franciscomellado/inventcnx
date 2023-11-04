from django.forms import ModelForm
from django.forms import DateInput, DateField, BooleanField, CheckboxInput,ModelChoiceField,CharField,widgets
from .models import (Inventario, Dispositivo, Software)
from django.contrib.contenttypes.forms import generic_inlineformset_factory

class Inventario_form(ModelForm):
#   def __init__(self, *args, **kwargs):
#     pass
    #   for field_name, field in self.fields.items():
    #       print(field_name,field)
    #       if isinstance(field, DateField):
    #         field.widget = DateInput(attrs={
    #             'class': 'form-control ml-6 datetimepicker', 
    #             'type': 'date'}
    #         )
    #       if isinstance(field, BooleanField):
    #         field.widget = BooleanField(attrs={
    #             'class': 'custom-control-input', 
    #             'type': 'date'}
    #         )  
        
            
  class Meta:
    model = Inventario
    fields = '__all__'
    exclude = ['id']
    
# ---- Formulario de Dispositivo --- 
class Dispositivo_form(ModelForm):
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
              field.widget.attrs['class'] = 'form-control'
        for field_name, field in self.fields.items():
            print(field_name,field)
            if isinstance(field, DateField):
                field.widget = DateInput(attrs={
                        'class': 'form-control datepicker',
                        'data-toggle': 'datetimepicker',
                        'data-target':"#id_" + field_name
                        }
                    )
       
  class Meta:
    model = Dispositivo
    fields = '__all__'
    exclude = ['id'] 
    widgets = {
            'date': widgets.DateInput(attrs={'type': 'date'})
        }
DispositivoInlineFormSet = generic_inlineformset_factory(
    Inventario,
    form=Dispositivo_form, 
    fields='__all__', 
    can_delete=False, 
    extra=1,
)

DispositivoInlineFormSetUpdate = generic_inlineformset_factory(
    Inventario,
    form=Dispositivo_form, 
    fields='__all__', 
    can_delete=False, 
    extra=0,
)

# ---- Formulario de Software --- 
class Software_form(ModelForm):
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
              field.widget.attrs['class'] = 'form-control'
        for field_name, field in self.fields.items():
            print(field_name,field)
            if isinstance(field, DateField):
                field.widget = DateInput(attrs={
                        'class': 'form-control datepicker',
                        'data-toggle': 'datetimepicker',
                        'data-target':"#id_" + field_name
                        }
                    )
            
        
  class Meta:
    model = Software
    fields = '__all__'
    exclude = ['id']   
    
    
SoftwareInlineFormSet = generic_inlineformset_factory(
    Inventario,
    form=Software_form, 
    fields='__all__', 
    can_delete=False, 
    extra=1,
)

SoftwareInlineFormSetUpdate = generic_inlineformset_factory(
    Inventario,
    form=Software_form, 
    fields='__all__', 
    can_delete=False, 
    extra=0,
)