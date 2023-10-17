from django.contrib import admin


from inventario.models import Proveedor, Estado, Marca, Dispositivo,Software, Inventario


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ["nombre", "codigo", "contacto"]
 
admin.site.register(Proveedor, ProveedorAdmin)
   
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ["nombre", "cantidad_licencias", "fecha_compra"]

admin.site.register(Software, SoftwareAdmin) 

class EstadoAdmin(admin.ModelAdmin):
    list_display = ["estado", "desripcion"]

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Marca)
admin.site.register(Dispositivo)

admin.site.register(Inventario)


    
    