from tkinter import Widget
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
            'Apellido': 'Apellido',
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
                'placeholder': 'Apellido',
                'required': 'true'
                
              }
            )
        }
    
    class area_form(ModelForm):
      class Meta:
        model = Area
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre',
            
        }
        
    class departamento_form(ModelForm):
      class Meta:
        model = Departamento
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre',
            
        }
