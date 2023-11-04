from django.contrib import admin
from .models import Departamento, Personas


admin.site.site_header = "Inventario Admin"

class PersonasAdmin(admin.ModelAdmin):
    model = Personas
    list_display = ("nombre", "apellido", "email", "area", "departamento",)
    list_filter = ["area"]
    search_fields = ["apellido"]


class DepartamentoAdmin(admin.ModelAdmin):
    model = Departamento
    list_display = ("nombre",)
    list_filter = ["nombre"]
    search_fields = ["nombre"]


admin.site.register(Personas, PersonasAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
