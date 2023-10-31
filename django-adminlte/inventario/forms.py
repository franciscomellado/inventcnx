from msilib.schema import CheckBox
from xmlrpc.client import Boolean
from django.forms import ModelForm
from django.forms import DateInput, DateField, BooleanField, CheckboxInput
from .models import (Inventario, Dispositivo, Software)
from django.contrib.contenttypes.forms import generic_inlineformset_factory
class Inventario_form(ModelForm):
  def __init__(self, *args, **kwargs):
        for field_name, field in self.fields.items():
            print(field_name,field)
            if isinstance(field, DateField):
              field.widget = DateInput(attrs={
                  'class': 'form-control auto-col ml-6', 
                  'type': 'date'}
              )
            elif isinstance(field, BooleanField):
              field.widget = CheckboxInput(attrs={
                    'class': 'form-check-input', 
                    'type': 'checkbox'}
              )
        for field in self.fields.values():
              field.widget.attrs['class'] = 'form-control-sm auto-col'
            
  class Meta:
    model = Inventario
    fields = '__all__'
    exclude = ['id']
    
# ---- Formulario de Dispositivo --- 
class Dispositivo_form(ModelForm):
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            print(field_name,field)
            if isinstance(field, DateField):
                field.widget = DateInput(attrs={
                    'class': 'form-control auto-col', 
                    'type': 'date'}
                    )
            for field in self.fields.values():
              field.widget.attrs['class'] = 'form-control-sm auto-col'
        # self.fields['student_date_of_birth'].widget = widgets.DateInput(
        #     attrs={
        #         'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
        #         'class': 'form-control'
        #         }
        #     )
  class Meta:
    model = Dispositivo
    fields = '__all__'
    exclude = ['id'] 
    
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
        for field_name, field in self.fields.items():
            print(field_name,field)
            if isinstance(field, DateField):
                field.widget = DateInput(attrs={
                    'class': 'form-control auto-col', 
                    'type': 'date'}
                    )
            for field in self.fields.values():
              field.widget.attrs['class'] = 'form-control-sm auto-col'
        # self.fields['student_date_of_birth'].widget = widgets.DateInput(
        #     attrs={
        #         'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
        #         'class': 'form-control'
        #         }
        #     )
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