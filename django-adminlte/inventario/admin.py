from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from inventario.models import Estado, Factura, Proveedor, Marca, TipoDispositivo, Dispositivo, Software, Inventario

class InventarioInline(GenericStackedInline):
    model = Inventario
    extra = 1

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo", "contacto")
    

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cantidad_licencias", "fecha_compra")
    inlines = [InventarioInline]
  


class DispositivoAdmin(admin.ModelAdmin):
    
    inlines = [InventarioInline]
 
    
    

    
admin.site.register(Estado)
admin.site.register(Marca)
admin.site.register(TipoDispositivo)
admin.site.register(Inventario)
admin.site.register(Factura)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Software, SoftwareAdmin)     
admin.site.register(Dispositivo, DispositivoAdmin)
