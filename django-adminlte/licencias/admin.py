from django.contrib import admin
from licencias.models import EstadoLic, TipoLicencia, Licencia, LicenciaUsuario

class LicenciaUsuarioAdmin(admin.StackedInline):
    model =LicenciaUsuario
    list_display = ['personas', 'fecha_asignada', 'fecha_registro']
    search_fields = ['persona__nombre', 'persona__apellido']
    extra=1
     
    
class PersonaAdmin(admin.ModelAdmin):
    inlines = [LicenciaUsuarioAdmin]

class LicenciaAdmin(admin.ModelAdmin):
    #fields = [("nombre", "numero_identificacion"), "software","tipo_licencia", "fecha_vencimiento",'estado','asignada']
    list_display = ['nombre', 'numero_identificacion', 'software', 'tipo_licencia', 'fecha_activacion','fecha_vencimiento', 'estado', 'asignada']
    readonly_fields = ['fecha_vencimiento']
    search_fields = [ 'numero_identificacion']
    list_filter = ['software', 'tipo_licencia', 'fecha_activacion', 'fecha_vencimiento']
    ordering = ['-fecha_activacion']
    inlines = [LicenciaUsuarioAdmin]

admin.site.register(EstadoLic)
admin.site.register(TipoLicencia)
admin.site.register(Licencia,LicenciaAdmin)
admin.site.register(LicenciaUsuario)
