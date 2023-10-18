from django.contrib import admin
from inventario.models import Estado, Proveedor, Marca, TipoDispositivo, Dispositivo, Software, Inventario

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ["nombre", "codigo", "contacto"]
 
admin.site.register(Proveedor, ProveedorAdmin)
   
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ["nombre", "cantidad_licencias", "fecha_compra"]

admin.site.register(Software, SoftwareAdmin) 

class EstadoAdmin(admin.ModelAdmin):
    list_display = ["estado"]

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Marca)

class TipoDispositoAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    
admin.site.register(TipoDispositivo, TipoDispositoAdmin)
admin.site.register(Dispositivo)

admin.site.register(Inventario)


    
    