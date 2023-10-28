from django import forms
from django.forms import ModelForm
from .models import Inventario
from django.contrib.contenttypes.forms import generic_inlineformset_factory
class Inventario_form(ModelForm):
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

  class Meta:
    model = Inventario
    fields = '__all__'
    exclude = ['id']
    
InventarioInlineFormSet = generic_inlineformset_factory(
    Inventario, fields='__all__', can_delete=False, extra=1,
)