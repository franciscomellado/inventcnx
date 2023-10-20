from mimetypes import init
from turtle import textinput
from django import forms
from django.forms import ModelForm
from .models import Area, Persona, Departamento
from django import forms

class Personas_form(ModelForm):
    class Meta:
        models = Persona
        fields = "__all__"
        labels = {
            'nombre': 'Nombre', 
            'apellido': 'Apellido',
            'email': 'Correo',
            'area': 'Area',
        }
        
        Widget = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre',
                    'required':'true'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo',
                    'required':'true'
                }
            )
        }
        
class Departamento_form(ModelForm):
    class Meta:
        models = Departamento
        fields = ['nombre']
        labels = {
            'nombre':'Nombre',
        }
    Widget = {
        'nombre': forms.TimeInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Nombre',
                'required':'true'
            }
        )
    }
    
    
    
    
    
    
    
    