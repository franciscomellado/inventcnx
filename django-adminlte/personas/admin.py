from django.contrib import admin
from .models import Departamento, Persona

admin.site.site_header = "Inventario Admin"

class PersonasAdmin(admin.ModelAdmin):
    model = Persona
    list_display = ("nombre", "apellido", "email",)
    search_fields = ["apellido"]


class DepartamentoAdmin(admin.ModelAdmin):
    model = Departamento
    list_display = ("gerencia",)
    list_filter = ["gerencia"]
    search_fields = ["gerencia"]


admin.site.register(Persona, PersonasAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
