from django.urls import path
from personas.views import *

app_name = "personas"
urlpatterns = [
    path("", PersonasListView.as_view(), name="index"),
    path("eliminar/<int:pk>", PersonasDeleteView.as_view(), name="eliminar"),
    path("crear", PersonasCreateView.as_view(), name="crear"),
    path("editar/<int:pk>", PersonasUpdateView.as_view(), name="editar"),
    
    
    path("departamento/", DepartamentoListView.as_view(), name="departamento"),
    path(
        "departamento/eliminar/<int:pk>",
        DepartamentoDeleteView.as_view(),
        name="departamentoeliminar",
    ),
    path(
        "departamento/crear", DepartamentoCreateView.as_view(), name="departamentocrear"
    ),
    path(
        "departamento/editar/<int:pk>",
        DepartamentoUpdateView.as_view(),
        name="departamentoeditar",
    ),
]
