from django.urls import path
from inventario.views import *

app_name = 'inventario'

urlpatterns = [
    path("", InventarioListWiews.as_view(), name="index"),
    # path('eliminar/<int:id>', PersonasDeleteWiews.as_view, name="eliminar"),
    # path('crear', PersonasCreateViews.as_view(), name="crear"),
    # path('editar/<int:id>', PersonasUpdateViews.as_view(), name="editar"),
    
]
