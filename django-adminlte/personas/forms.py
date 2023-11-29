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
       
        # labels = {
        #     "nombre": "Nombre", 
        #     "apellido": "Apellido",
        #     "email": "Correo",
        #     "usuario": "Usuario",
        #     "gerencia": "Gerencia",
        # }
        
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control col-sm-10",
                    "placeholder": "Nombre",
                    "required":"true",
                    
                },
                
            ),
           
            "apellido": forms.TextInput(
                attrs={
                    "class": "form-control col-sm-10",
                    "placeholder": "Apellido",
                    "required":"true"
                }
            ),
            
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control col-sm-10",
                    "placeholder": "Correo",
                    "required":"true"
                }
            ),
            
            "usuario": forms.TextInput(
                attrs={
                    "class": "form-control col-sm-10",
                    "placeholder": "usuario",
                    "required": False
                }
            ),
            
            "gerencia": forms.Select(
                attrs={
                    "class": "form-control col-sm-10",
                    
                    "required":"true"
                }
            )
        }
        
        
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
    
    
    
    
    
    
    
    