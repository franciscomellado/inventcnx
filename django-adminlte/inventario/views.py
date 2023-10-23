from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from .models import Inventario
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import *
from django.contrib import messages

class InventarioListWiews(ListView):
    models: Inventario
    queryset = Inventario.objects.all()
    template_name = 'inventario/inventario_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    