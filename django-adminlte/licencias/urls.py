from django.urls import path
from licencias.views import *

app_name = "licencias"
urlpatterns = [
    path("", LicenciasListView.as_view(), name="index"),
    path("eliminar/<int:pk>", LicenciassDeleteView.as_view(), name="eliminar"),
    path("crear", LicenciasCreateView.as_view(), name="crear"),
    path("editar/<int:pk>", LicenciasUpdateView.as_view(), name="editar"),
    
   
]
