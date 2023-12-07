from mimetypes import init
from turtle import textinput
from django import forms
from django.forms import ModelForm
from .models import Persona, Departamento
from django import forms

class Personas_form(ModelForm):
    class Meta:
        model = Persona
        fields = "__all__"
        
class Departamento_form(ModelForm):
    class Meta:
        model = Departamento
        fields = ["gerencia"]
        labels = {
            "gerencia":"Gerencia",
        }
    Widget = {
        "gerencia": forms.TimeInput(
            attrs={
                "class":"form-control",
                "placeholder": "gerencia",
                "required":"true"
            }
        )
    }
    
    
    
    
    
    
    
    