from mimetypes import init
from turtle import textinput
from django.forms import ModelForm
from .models import Area, Departamento, Personas
from django import forms



class Personas_form(ModelForm):
    class Meta:
        model = Personas
        fields = "__all__"
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo',
            'area': 'Area'
        }
        
        widgets = {
            'nombre': forms.TextInput(
              attrs={
                'class': 'form-control',
                'placeholder': 'Nombre', 
                'required': 'true'
              } 
            ),
            
            'apellido': forms.TextInput(
              attrs={
                'class': 'form-control',
                'placeholder': 'Apellido',
                'required': 'true'
              }
            ),
            
            'email': forms.EmailInput(
              attrs={
                 'class': 'form-control',
                'placeholder': 'Correo',
                'required': 'true'
              }
            ),
            
            'area': forms.Select (
              attrs={
                 'class': 'select2 form-control',
                'placeholder': 'Apellido',
                'required': 'true'
              }
            ),
            
            'departamento': forms.Select(
              attrs={
                 'class': 'select2 form-control',
                'placeholder': 'Apellido',
                'required': 'true'
                
              }
            )
        }
    
class Area_form(ModelForm):
      class Meta:
        model = Area
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre',
        }
        widgets = {
            'nombre': forms.TextInput(
              attrs={
                'class': 'form-control',
                'placeholder': 'Nombre', 
                'required': 'true'
              } 
            )
        }
class Departamento_form(ModelForm):
      class Meta:
        model = Departamento
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre',
            
        }
      widgets = {
            'nombre': forms.TextInput(
              attrs={
                'class': 'form-control',
                'placeholder': 'Nombre', 
                'required': 'true'
              } 
            )
      }