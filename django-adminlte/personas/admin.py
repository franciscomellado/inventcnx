from django.contrib import admin
from personas.models import Personas,Area,Departamento
# Register your models here.

admin.site.site_header = "Inventario Admin"

class PersonasAdmin(admin.ModelAdmin):
    model = Personas
    list_display = ("nombre", "apellido", "email", "area", "departamento",)
    list_filter = ["area"]
    search_fields = ["apellido"]

class AreaAdmin(admin.ModelAdmin):
    model = Area
    list_display = ("nombre",)
    list_filter = ["nombre"]
    search_fields = ["nombre"]

class DepartamentoAdmin(admin.ModelAdmin):
    model = Departamento
    list_display = ("nombre",)
    list_filter = ["nombre"]
    search_fields = ["nombre"]


admin.site.register(Personas, PersonasAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
