from django.urls import path
from inventario.views import *

app_name = 'inventario'
urlpatterns = [
    path("", InventarioListViews.as_view(), name="index"),
    path("crear", InventarioCreateView.as_view(), name="crear"),
    path("editar/<int:pk>", InventarioUpdateView.as_view(), name="editar"),
    path("eliminar/<int:pk>", InventarioDeleteView.as_view(), name="eliminar"), 
    #path("detalle/<int:id>", InventarioDetailView.as_view(), name="detalle"),

    ## Dispositivos
    path("dispositivo/", DispositivoListViews.as_view(), name="index_disp"),
    path("dispositivo/crear", DispositivoCreateView.as_view(), name="crear_disp"),
    path("dispositivo/editar/<int:pk>", DispositivoUpdateView.as_view(), name="editar_disp"),
    path("dispositivo/eliminar/<int:pk>", DispositivoDeleteView.as_view(), name="eliminar_disp"),
    #path("dispositivo/detalle/<int:id>", DispositivoDetailView.as_view(), name="detalle_disp"),
    
    ## Software
    path("software/", SoftwareListViews.as_view(), name="index_soft"),
    path("software/crear", SoftwareCreateView.as_view(), name="crear_soft"),
    path("software/editar/<int:pk>", SoftwareUpdateView.as_view(), name="editar_soft"),
    path("software/eliminar/<int:pk>", SoftwareDeleteView.as_view(), name="eliminar_soft"),
    #path("software/detalle/<int:id>", SoftwareDetailView.as_view(), name="detalle_soft"),
    
    ##Proveedor
    ## Software
    path("proveedor/", ProveedorListViews.as_view(), name="index_prove"),
    path("proveedor/crear", ProveedorCreateView.as_view(), name="crear_prove"),
    path("proveedor/editar/<int:pk>", ProveedorUpdateView.as_view(), name="editar_prove"),
    path("proveedor/eliminar/<int:pk>", ProveedorDeleteView.as_view(), name="eliminar_prove"),
    #path("proveedor/detalle/<int:id>", ProveedorDetailView.as_view(), name="detalle_prove"),
]
