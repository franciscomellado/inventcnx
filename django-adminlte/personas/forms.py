from django import forms
from personas.models import Usuario

class Personas_forms(forms.ModelForm):
    class Meta:
        models = Usuario
        fields = "__all__"
        
        