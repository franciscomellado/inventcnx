from django.shortcuts import render
from django.views.generic import TemplateView

class Personaindex(TemplateView):
    template_name = 'personas/data.html'


# def index(request):
#     return render(request, "personas/data.html")
