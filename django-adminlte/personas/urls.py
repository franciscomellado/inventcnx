from django.urls import path
from personas.views import *

app_name = "personas"
urlpatterns = [
    path("", PersonasListView.as_view(), name="index"),
    path("eliminar/<int:pk>", PersonasDeleteView.as_view(), name="eliminar"),
    path("crear", PersonasCreateView.as_view(), name="crear"),
    path("editar/<int:pk>", PersonasUpdateView.as_view(), name="editar"),
    
    ## Departamentos
    path("dpto/", DepartamentoListView.as_view(), name="dpto"),
    path(
        "dpto/eliminar/<int:pk>",
        DepartamentoDeleteView.as_view(),
        name="eliminar_dpto",
    ),
    path("dpto/crear", DepartamentoCreateView.as_view(), name="crear_dpto"),
    path(
        "dpto/editar/<int:pk>",
        DepartamentoUpdateView.as_view(),
        name="editar_dpto",
    ),
]
