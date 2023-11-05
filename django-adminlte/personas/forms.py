from django import forms
from django.forms import ModelForm
from .models import Persona, Departamento
from django import forms

class Personas_form(ModelForm):
    class Meta:
        model = Persona
        fields = "__all__"
        labels = {
            'nombre': 'Nombre', 
            'apellido': 'Apellido',
            'email': 'Correo',
            'gerencia': 'Gerencia',
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
                    'placeholder': 'Apellido',
                    'required':'true'
                }
            ),
            
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo',
                    'required':'true'
                }
            ),
            
            'gerencia': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Gerencia',
                    'required':'true'
                }
            )
        }
        
class Departamento_form(ModelForm):
    class Meta:
        model = Departamento
        fields = ['gerencia']
        labels = {
            'gerencia':'Gerencia',
        }
    Widget = {
        'gerencia': forms.TimeInput(
            attrs={
                'class':'form-control',
                'placeholder': 'gerencia',
                'required':'true'
            }
        )
    }
    