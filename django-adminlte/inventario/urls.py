from django.urls import path
from inventario.views import *

app_name = 'inventario'

urlpatterns = [
    path("", InventarioListViews.as_view(), name="index"),
    path("crear", InventarioCreateView.as_view(), name="crear"),
    path("editar/<int:pk>", InventarioUpdateView.as_view(), name="editar"),
    path("eliminar/<int:pk>", InventarioDeleteView.as_view(), name="eliminar"),
    #path("detalle/<int:id>", InventarioDetailView.as_view(), name="detalle"),
    
    # path('eliminar/<int:id>', PersonasDeleteWiews.as_view, name="eliminar"),
    # path('crear', PersonasCreateViews.as_view(), name="crear"),
    # path('editar/<int:id>', PersonasUpdateViews.as_view(), name="editar"),
    
]
