from django.urls import path
from personas.views import *

app_name = 'personas'

urlpatterns = [
    path("", PersonasListWiews.as_view(), name="index"),
    path('editar/<int:id>', PersonasUpdateViews.as_view(), name="editar"),
    path('crear', PersonasCreateViews.as_view(), name="crear"),
    path('eliminar/<int:id>', PersonasDeleteWiews.as_view, name="eliminar"),
    
]
